from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Calender(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.CharField(max_length=200, default='')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
