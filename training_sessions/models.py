from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from dogs.models import Dog
from admin_users.models import Trainer

# Create your models here.


class Session(models.Model):
    trainer = models.ManyToManyField(Trainer)
    activity_name = models.CharField(max_length=50)
    dogs_in_session = models.ManyToManyField(Dog)
    time_started = models.DateTimeField(default=timezone.now)
    time_ended = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.activity_name


class Report(models.Model):
    dog_name = models.ForeignKey(Dog, on_delete=CASCADE)
    sessions = models.ManyToManyField(Session)
    time_created = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
