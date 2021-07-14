from django.shortcuts import render
from django.contrib.auth.models import User
from admin_users.models import Trainer
from notifications.models import Notification

# Create your views here.


def notifications_view(request, user_id: int):
    this_user = User.objects.get(id=request.user.id)
    # mention = f'@{request.user}'
    all_notifications = Notification.objects.filter(
        send_to=this_user).exclude(seen_by_user=True)
    count = 0
    for item in all_notifications:
        count += 1
        item.seen_by_user = True
        item.save()
    for item in all_notifications:
        if item.seen_by_user == True:
            item.delete()
    return render(request, 'notifications.html', {'all_notifications': all_notifications, 'count': count, 'this_user': this_user})
