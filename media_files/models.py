from django.db import models

# Create your models here.


class MediaFile(models.Model):
    dog = models.ForeignKey(to='dogs.Dog', on_delete=models.CASCADE)
    image = models.FileField(
        upload_to='static/image_media/', null=True, blank=True)

    # def __str__(self):
    #     return self.image
