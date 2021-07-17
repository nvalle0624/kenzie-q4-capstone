
# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, reverse
from notifications.models import Notification
from media_files.models import UserProfilePic, DogProfilePic
from media_files.forms import MediaForm
from dogs.models import Dog


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


def upload_dog_profile_pic(request, dog_id: int):
    all_notifications = Notification.objects.filter(
        send_to=request.user).exclude(seen_by_user=True)
    num_notifications = 0
    for notification in all_notifications:
        num_notifications += 1
    this_dog = Dog.objects.get(id=dog_id)
    if request.method == 'POST':
        profile_pic = ''
        if DogProfilePic.objects.filter(dog=this_dog):
            profile_pic = DogProfilePic.objects.get(dog=this_dog)
            profile_pic.delete()
        image_form = MediaForm(request.POST, request.FILES)
        if image_form.is_valid():
            data = image_form.cleaned_data
            new_image = DogProfilePic.objects.create(
                dog=this_dog,
                image=data['media'],
            )
            homepage = ''
            if request.user.is_staff:
                homepage = 'trainer_home'
            else:
                homepage = 'client_home'
            return HttpResponseRedirect(reverse(homepage, args=[request.user.id]))
    image_form = MediaForm()
    return render(request, 'upload_profile_pic.html', {'image_form': image_form, 'num_notifications': num_notifications, 'all_notifications': all_notifications})
