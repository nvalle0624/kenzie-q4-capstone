from admin_users.models import Trainer
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Message(models.Model):
    text = models.TextField(max_length=140)
    time_posted = models.DateTimeField(default=timezone.now)
    sent_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_by')
    send_to = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, blank=True, related_name='send_to')
