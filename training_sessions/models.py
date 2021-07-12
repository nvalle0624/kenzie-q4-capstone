from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField
from django.utils import timezone
from dogs.models import Dog

# Create your models here.


class Session(models.Model):
    trainer = models.ForeignKey()
    dogs_in_session = models.ManyToManyField(Dog)
    activity_name = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    completed = models.BooleanField()
    notes = models.TextField(max_length=400)


class Report(models.Model):
    dog_name = models.ForeignKey(Dog, on_delete=CASCADE)
    time_created = models.DateTimeField(default=timezone.now)
