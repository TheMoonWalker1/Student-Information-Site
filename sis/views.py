from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets
from api import permissions
from .serializers import *
from .forms import *


# Template Views
def manageClassesView(request):
    if request.user.is_staff is False:
        raise Http404("You are not a valid User")
    data = {
        'success': False,
        'failure': False,
        'classes': Class.objects.all().filter(teacher=request.user)
    }
    if request.method == "POST":
        categories = []
        i = 1
        while True:
            if f"category_name_{i}" not in request.POST or request.POST.get(f"category_name_{i}") is None or request.POST.get(f"category_name_{i}") == "":
                break
            categories.append(
                (
                    request.POST.get(f"category_name_{i}"),
                    float(request.POST.get(f"category_weight_{i}"))
                )
            )
            i += 1

        if sum(n for _, n in categories) != 100:
            data['failure'] = True
            data['message'] = f"The {i - 1} categories you have inputted into the system do not add up to 100, please try again."
        else:
            cats = [Category(name=name, weight=weight, value=0) for name, weight in categories]

            new_class = Class(name=request.POST.get('class_name'), teacher=request.user,
                              period=request.POST.get('class_period'), room=request.POST.get('class_room_number'),)
            if new_class:
                new_class.save()
            for cat in cats:
                cat.save()
                new_class.categories.add(cat)

            data['success'] = True
            data['code'] = new_class.code

    return render(request, "staff/manage_classes.html", data)


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

