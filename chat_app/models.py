from django.db import models
from datetime import datetime

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100, default='Untitled Room')

    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.CharField(max_length=10000, default='')
    timestamp = models.DateTimeField(default=datetime.now())
    user_name = models.CharField(max_length=100, default='')
    room = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.id)
