from django.db import models
import uuid
from django.contrib.auth import get_user_model


# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=300, blank=False)
    teacher = models.ForeignKey(get_user_model(), blank=False, null=True, related_name="teacher", on_delete=models.SET_NULL)
    student = models.ForeignKey(get_user_model(), blank=False, null=True, related_name="student", on_delete=models.SET_NULL)
    period = models.IntegerField(blank=False)
    room = models.CharField(max_length=10, blank=False)
    grade = models.FloatField(blank=False)

    def __str__(self):
        return self.name + f' - Period: {self.period}'

    def letter_grade(self):
        score = round(self.grade)
        if score >= 90:
            return "A"
        if 90 > score >= 80:
            return "B"
        if 80 > score >= 70:
            return "C"
        if 70 > score >= 60:
            return "D"
        if 60 > score:
            return "F"


class School(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, unique=True)
    staff = models.ManyToManyField(get_user_model(), related_name="staff", blank=False)
    students = models.ManyToManyField(get_user_model(), related_name="students", blank=False)
    classes = models.ManyToManyField(Class, blank=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name
