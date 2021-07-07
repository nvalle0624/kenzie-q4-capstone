from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phone_field import PhoneField
# Create your models here.


# Admin/trainer
# Name - text
# Number - phone/integer?
# Email - email
# Monthly availability - choices, date/time fields?
# Booked sessions - list, text or date/time fields?
# Certifications- text, choices
# Field expertise(trainer, walker, hiker, runner, behavior) - text, choices



class Trainer(models.Model):
    EXPERTISE_CHOICES = (
    ('T', 'Trainer'),
    ('W', 'Walker'),
    ('H', 'Hiker'),
    ('R', 'Runner'),
    ('B', 'Behavioral')
    

)
    admin_user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=254)
    cert = models.CharField(max_length=50)
    field_of_expertise = models.CharField(max_length=1, choices=EXPERTISE_CHOICES)

    def __str__(self):
        return self.name