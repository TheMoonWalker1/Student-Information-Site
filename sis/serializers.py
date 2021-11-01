from rest_framework import serializers
from django.contrib.auth import get_user_model
from sis.models import School, Class, Profile


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['url', 'name', 'staff', 'students', 'classes', 'id']


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Class
        fields = ['url', 'name', 'teacher', 'student', 'period', 'room', 'grade']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'gender', 'fathers_name', 'mothers_name', 'guardian_name', 'dob', 'phone', 'mobile', 'address']
