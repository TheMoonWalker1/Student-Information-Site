from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'email', 'first_name', 'last_name', 'groups', 'is_staff', 'is_superuser']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
