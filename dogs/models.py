from django.db import models
from users.models import Client
from phone_field import PhoneField
import os
from bananadog.settings import BASE_DIR
# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(
        Client, on_delete=models.CASCADE, null=True)
    breed = models.CharField(max_length=40, blank=True)
    age_years = models.PositiveSmallIntegerField(default=0, blank=True)
    age_months = models.PositiveSmallIntegerField(default=0, blank=True)
    vet_name = models.CharField(max_length=30, blank=True)
    vet_number = PhoneField(blank=True, help_text='Contact Number')
    vet_address = models.CharField(max_length=200, blank=True)
    special_needs = models.TextField(blank=True)
    extra_notes = models.TextField(blank=True)
    booked_sessions = models.ManyToManyField(
        to="training_sessions.Session", default=None, blank=True)
    no_match_dogs = models.ManyToManyField('self', default=None, blank=True)
    profile_pic = models.ForeignKey(
        to='media_files.DogProfilePic', blank=True, null=True, on_delete=models.SET_NULL, related_name='dog_profile_pic')

    def __str__(self):
        return self.name
