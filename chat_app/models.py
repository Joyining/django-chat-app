from django.db import models
import django.utils.timezone

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100, default='Untitled Room')

    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.CharField(max_length=10000, default='')
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    user_name = models.CharField(max_length=100, default='')
    room_id = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.id)
