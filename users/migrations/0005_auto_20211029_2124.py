# Generated by Django 3.2.8 on 2021-10-30 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customuser_grades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='classes',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='school',
        ),
    ]
