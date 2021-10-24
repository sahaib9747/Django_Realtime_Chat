from datetime import datetime

from django.db import models
from django.db.models.fields import DateTimeField, TextField

# Create your models here.
class Room(models.Model):
    name = models.TextField(blank=False)
    password = models.TextField(blank=False)
    
    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    room = TextField(blank=False)
    user = TextField(blank=False)
    message = TextField(blank=False)
    date = DateTimeField(default=datetime.now())
