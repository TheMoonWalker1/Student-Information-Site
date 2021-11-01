from django.db import models
import uuid
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField


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

def create_student_code():
    return uuid.uuid4().hex[:8].upper()

class School(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, unique=True)
    staff = models.ManyToManyField(get_user_model(), related_name="staff", blank=False)
    students = models.ManyToManyField(get_user_model(), related_name="students", blank=False)
    classes = models.ManyToManyField(Class, blank=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    staff_code = models.UUIDField(default=uuid.uuid4, editable=False)
    student_code = models.CharField(max_length=5, default=create_student_code(), unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=1, blank=False, choices=GENDER_CHOICES)
    fathers_name = models.CharField(max_length=50, blank=False)
    mothers_name = models.CharField(max_length=50, blank=False)
    guardian_name = models.CharField(max_length=50, blank=False)
    dob = models.DateField(name="Date Of Birth")
    phone = PhoneNumberField(blank=False)
    mobile = PhoneNumberField(blank=True)
    address = models.CharField(max_length=300, blank=False)