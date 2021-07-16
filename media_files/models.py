from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DogMediaFile(models.Model):
    dog = models.ForeignKey(to='dogs.Dog', on_delete=models.CASCADE)
    image = models.FileField(
        upload_to='static/image_media/', null=True, blank=True)

    # def __str__(self):
    #     return self.image


class UserMediaFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(
        upload_to='static/image_media/', null=True, blank=True)
