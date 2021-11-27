from rest_framework import routers
from django.urls import path, include

from users import views as u_views
from sis import views as s_views

router = routers.DefaultRouter()
router.register(r'users', u_views.UserViewSet)
router.register(r'groups', u_views.GroupViewSet)
router.register(r'schools', s_views.SchoolViewSet)
router.register(r'classes', s_views.ClassViewSet)
router.register(r'profiles', s_views.ProfileViewSet)
router.register(r'categories', s_views.CategoryViewSet)
router.register(r'entries', s_views.EntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
