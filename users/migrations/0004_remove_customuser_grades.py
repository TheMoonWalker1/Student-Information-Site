# Generated by Django 3.2.8 on 2021-10-30 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211029_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='grades',
        ),
    ]
