from django.db import models
from users.models import Client
from phone_field import PhoneField
# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(
        Client, on_delete=models.CASCADE)
    breed = models.CharField(max_length=40)
    age_years = models.IntegerField(default=0)
    age_months = models.IntegerField(default=0)
    vet_name = models.CharField(max_length=30)
    vet_number = PhoneField(blank=True, help_text='Contact Number')
    vet_address = models.CharField(max_length=200)
    special_needs = models.TextField(blank=True)
    extra_notes = models.TextField(blank=True)
    # classes_completed =
    # booked_sessions =
    # media =
    no_match_dogs = models.ManyToManyField('self', default=None, blank=True)

    def __str__(self):
        return self.name
