from django import forms
from .models import School, Class, Profile


class AddSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name']
