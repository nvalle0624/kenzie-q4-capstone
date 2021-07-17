
# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, reverse
from notifications.models import Notification
from media_files.models import UserProfilePic
from media_files.forms import MediaForm
from media_files.models import UserMediaFile


def upload_profile_pic(request):
    trainer_notifications = Notification.objects.filter(
        send_to=request.user).exclude(seen_by_user=True)
    num_notifications = 0
    for notification in trainer_notifications:
        num_notifications += 1
    if request.method == 'POST':
        profile_pic = ''
        if UserProfilePic.objects.filter(user=request.user):
            profile_pic = UserProfilePic.objects.get(user=request.user)
            profile_pic.delete()
        image_form = MediaForm(request.POST, request.FILES)
        if image_form.is_valid():
            data = image_form.cleaned_data
            new_image = UserProfilePic.objects.create(
                user=request.user,
                image=data['media'],
            )
            homepage = ''
            if request.user.is_staff:
                homepage = 'trainer_home'
            else:
                homepage = 'client_home'
            return HttpResponseRedirect(reverse(homepage, args=[request.user.id]))
    image_form = MediaForm()
    return render(request, 'upload_profile_pic.html', {'image_form': image_form, 'num_notifications': num_notifications})
