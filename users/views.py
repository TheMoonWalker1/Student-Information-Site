from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework import viewsets
import uuid

from api import permissions
from .serializers import UserSerializer, GroupSerializer

from sis.models import School


def registerView(request):
    data = {
        'success': False,
        'failure': False,
    }
    if request.method == "POST":
        email = request.POST.get('username')
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        password = request.POST.get('password')
        code = request.POST.get('code')

        user = None
        if len(code) == 8 and School.objects.get(student_code=code):
            try:
                user = get_user_model().objects.create_user(email=email, password=password, first_name=first, last_name=last)
                School.objects.get(student_code=code).students.add(user)
            except ValueError as v:
                data['exception'] = str(v)
                data['failure'] = True
        elif len(code) == 36 and School.objects.get(staff_code=uuid.UUID(code)):
            try:
                user = get_user_model().objects.create_staff(email=email, password=password, first_name=first, last_name=last)
                School.objects.get(staff_code=code).staff.add(user)
            except ValueError as v:
                data['exception'] = str(v)
                data['failure'] = True
        else:
            data['exception'] = "Invalid Code, please try again."
            data['failure'] = True

        if user:
            user.save()
            data['user'] = user
            data['success'] = True
            return redirect('login')

    elif request.user.is_authenticated:
        return redirect('home')

    return render(request, 'registration/register.html', data)


# Serializers
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AdminAuthenticationPermission]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AdminAuthenticationPermission]
