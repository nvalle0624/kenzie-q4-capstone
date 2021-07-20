from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.


class DogMediaFile(models.Model):
    dog = models.ForeignKey(to='dogs.Dog', on_delete=models.CASCADE)
    image = models.FileField(
        upload_to='static/image_media/', null=True, blank=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])])


class DogProfilePic(models.Model):
    dog = models.ForeignKey(to='dogs.Dog', on_delete=models.CASCADE)
    image = models.FileField(
        default='settings.STATICFILES_DIRS/base/dog_default_pic.jpg', upload_to='static/profile_pics/', null=True, blank=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])])


class UserMediaFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(
        upload_to='static/image_media/', null=True, blank=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])])


class UserProfilePic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(
        default='settings.STATICFILES_DIRS/base/default_profile_image.jpg', upload_to='static/profile_pics/', null=True, blank=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])])
