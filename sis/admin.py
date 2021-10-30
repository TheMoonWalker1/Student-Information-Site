from django.contrib import admin
from sis.models import Class, School
from users.models import CustomUser

# Register your models here.

admin.site.register(Class)
admin.site.register(School)
admin.site.register(CustomUser)
