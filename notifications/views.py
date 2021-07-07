from django.shortcuts import render
from notifications.models import Notification

# Create your views here.


def notification_view(request, user_id: int):
    mention = f'@{request.user}'
    all_notifications = Notification.objects.filter(
        text__contains=mention).exclude(seen_by_user=True)
    count = 0
    for item in all_notifications:
        count += 1
        item.seen_by_user = True
        item.save()
    return render(request, 'notifications.html', {'all_notifications': all_notifications, 'count': count})
