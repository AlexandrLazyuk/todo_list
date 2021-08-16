from django.utils import timezone
from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=100)
    checked = models.BooleanField(default=False)
