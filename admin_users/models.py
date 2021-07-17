from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phone_field import PhoneField


class Trainer(models.Model):
    EXPERTISE_CHOICES = (
        ('Trainer', 'Trainer'),
        ('Walker', 'Walker'),
        ('Hiker', 'Hiker'),
        ('Runner', 'Runner'),
        ('Behaviorist', 'Behaviorist')


    )
    admin_user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=254)
    cert = models.CharField(max_length=50, blank=True)
    field_of_expertise = models.CharField(
        max_length=11, choices=EXPERTISE_CHOICES)
    profile_pic = models.FileField(
        upload_to='static/profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.full_name
