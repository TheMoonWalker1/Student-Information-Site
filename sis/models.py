from django.db import models
import uuid


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name
