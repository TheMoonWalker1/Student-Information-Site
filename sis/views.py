from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from api import permissions
from .serializers import *


# Create your views here.
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

