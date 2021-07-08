from django.db import models
# from django.contrib.auth.models import User
from all_messages.models import Message


# Create your models here.


class Notification(Message):
    # text = models.TextField(max_length=140)
    # sent_by = models.ForeignKey(User, on_delete=models.CASCADE)
    seen_by_user = models.BooleanField(default=False)
    # time_posted = models.DateTimeField(auto_now_add=True)
