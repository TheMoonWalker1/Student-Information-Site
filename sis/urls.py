from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name="student/home.html", ), ), name='home'),
    path('manage_schools/', login_required(manageSchoolsView), name='manage_schools'),
    path('manage_classes/', login_required(manageClassesView), name='manage_classes')
    path('classes/', login_required(), name='classes')
]
