from django.db import models
from users.models import Client
from phone_field import PhoneField
# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(
        Client, on_delete=models.CASCADE)
    breed = models.CharField(max_length=40)
    age_years = models.PositiveSmallIntegerField(default=0)
    age_months = models.PositiveSmallIntegerField(default=0)
    vet_name = models.CharField(max_length=30)
    vet_number = PhoneField(blank=True, help_text='Contact Number')
    vet_address = models.CharField(max_length=200)
    special_needs = models.TextField(blank=True)
    extra_notes = models.TextField(blank=True)
    booked_sessions = models.ManyToManyField(
        to="training_sessions.Session", default=None, blank=True)
    img_media = models.FileField(
        upload_to='static/img_media/', null=True, blank=True)
    profile_pic = models.FileField(
        upload_to='static/img_media/profiles/', null=True, blank=True)
    no_match_dogs = models.ManyToManyField('self', default=None, blank=True)
    # reports = models.ForeignKey(
    #     to="training_sessions.Report", on_delete=models.CASCADE, blank=True, default=None)

    def __str__(self):
        return self.name
