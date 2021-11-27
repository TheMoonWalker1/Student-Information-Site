from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets
from api import permissions
from .serializers import *
from .forms import *


# Template Views
def manageSchoolsView(request):
    if request.user.is_superuser is False:
        return Http404("You are not a valid User")
    data = {
        'success': False,
        'failure': False,
        'schools': School.objects.all()
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
    elif request.user.is_authenticated:
        data['form'] = AddSchoolForm()
    else:
        raise Http404("You are not a valid User")
    return render(request, 'superuser/manage_schools.html', data)


# Serializer Views
class EntryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.AdminAuthenticationPermission]


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AdminAuthenticationPermission]


class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.AdminAuthenticationPermission]


class ClassViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [permissions.AdminAuthenticationPermission]


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AdminAuthenticationPermission]

