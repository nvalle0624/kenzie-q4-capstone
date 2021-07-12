from django.db import models
from all_messages.models import Message


# Create your models here.


class Notification(Message):
    seen_by_user = models.BooleanField(default=False)
