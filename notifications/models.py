from django.db import models
from all_messages.models import Message
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Notification(models.Model):
    text = models.TextField(max_length=140)
    time_posted = models.DateTimeField(default=timezone.now)
    sent_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_by_notification')
    send_to = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, blank=True, related_name='send_to_notification')

    seen_by_user = models.BooleanField(default=False)
