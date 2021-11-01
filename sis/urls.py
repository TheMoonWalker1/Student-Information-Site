from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
# from .views import *

urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name="home/home.html",),), name='home'),
]
