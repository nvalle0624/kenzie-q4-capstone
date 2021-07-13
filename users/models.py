from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from phone_field import PhoneField


class Client(models.Model):
    name = models.CharField(max_length=60)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=300)
    # phone field from: https://pypi.org/project/django-phone-field/
    phone_contact = PhoneField(
        blank=True, help_text='Contact Number')

    dogs_owned = models.ManyToManyField(
        to="dogs.Dog", default=None, blank=True)

    def __str__(self):
        return self.name
