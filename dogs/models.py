from django.db import models
from users.models import Client

# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(
        Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
