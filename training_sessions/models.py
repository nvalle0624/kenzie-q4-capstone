from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from dogs.models import Dog

# Create your models here.


class Session(models.Model):
    # trainer = add admin/trainer user relationship here
    activity_name = models.CharField(max_length=50)
    dogs_in_session = models.ManyToManyField(Dog)


class Report(models.Model):
    dog_name = models.ForeignKey(Dog, on_delete=CASCADE)
    # report = models.models.TextField()
    time_created = models.DateTimeField(default=timezone.now)
