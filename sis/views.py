from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from rest_framework import viewsets
from api import permissions
from .serializers import *
from .forms import *


# Template Views
def manageSchoolsView(request):
    data = {
        'success': False,
        'failure': False,
    }
    if request.method == "POST":
        form = AddSchoolForm(request.POST)
        if form.is_valid():
            school = form.save()
            data['success'] = True
            data['school'] = school
        else:
            data['form'] = AddSchoolForm()
            data['failure'] = True
    elif request.user.is_authenticated and request.user.is_superuser:
        data['form'] = AddSchoolForm()
    else:
        raise Http404("You are not a valid User")
    return render(request, 'superuser/manage_schools.html', data)


# Serializer Views
class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.AdminAuthenticationPermission]


class ClassViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [permissions.AdminAuthenticationPermission]


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AdminAuthenticationPermission]

