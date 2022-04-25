# Generated by Django 3.2.9 on 2022-01-05 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sis', '0008_auto_20211126_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='grade',
        ),
        migrations.AddField(
            model_name='category',
            name='assignments',
            field=models.ManyToManyField(blank=True, related_name='assignments', to='sis.Entry'),
        ),
        migrations.AlterField(
            model_name='class',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='school',
            name='student_code',
            field=models.CharField(default='AF5F1564', editable=False, max_length=5, unique=True),
        ),
    ]