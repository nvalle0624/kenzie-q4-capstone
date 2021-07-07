from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from phone_field import PhoneField
# from dogs.models import Dog


class Client(models.Model):
    name = models.CharField(max_length=60)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=300)
    # phone field from: https://pypi.org/project/django-phone-field/
    phone_contact = PhoneField(blank=True, help_text='Contact Number')

    # booked_sessions = upcoming sessions, many to many?, should show all past and future sessions from training sessions model
    dogs_owned = models.ManyToManyField(
        to="dogs.Dog", default=None, blank=True)
    # reports = foreign key or one to one with reports model in training sessions

    def __str__(self):
        return self.name
