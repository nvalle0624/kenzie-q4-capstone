from users.models import Client
from admin_users.models import Trainer
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponseRedirect, reverse
from dogs.models import Dog
from dogs.forms import DogProfileForm
from media_files.models import DogMediaFile, DogProfilePic
from media_files.forms import MediaForm
from notifications.models import Notification
from django.views.generic import UpdateView
import os

# Create your views here.


def dog_profile_form_view(request):
    if request.user.is_staff == False:
        this_client = Client.objects.get(user=request.user)
    if request.method == 'POST':
        form = DogProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_dog = Dog.objects.create(
                name=data['name'],
                owner=this_client,
                breed=data['breed'],
                age_years=data['age_years'],
                age_months=data['age_months'],
                vet_name=data['vet_name'],
                vet_number=data['vet_number'],
                vet_address=data['vet_address'],
                special_needs=data['special_needs'],
                extra_notes=data['extra_notes'],
            )
            this_client.dogs_owned.add(new_dog)
            return HttpResponseRedirect(reverse('client_home', args=[this_client.id]))
    form = DogProfileForm()
    return render(request, 'dog_profile_form.html', {'form': form, 'this_client': this_client})


def dog_profile_view(request, dog_id: int):
    this_dog = Dog.objects.get(id=dog_id)
    image_files = DogMediaFile.objects.filter(dog=this_dog)
    all_trainers = Trainer.objects.all()
    user_notifications = Notification.objects.filter(
        send_to=request.user).exclude(seen_by_user=True)
    num_notifications = 0
    for notification in user_notifications:
        num_notifications += 1
    profile_pic = ''
    if DogProfilePic.objects.filter(dog=this_dog):
        profile_pic = DogProfilePic.objects.get(dog=this_dog)
    if request.method == 'POST':
        image_form = MediaForm(request.POST, request.FILES)
        if image_form.is_valid():
            data = image_form.cleaned_data
            new_image = DogMediaFile.objects.create(
                dog=this_dog,
                image=data['media'],
            )
            this_user = ''
            if request.user.is_staff:
                this_user = Trainer.objects.get(admin_user=request.user)
            else:
                this_user = Client.objects.get(user=request.user)
            return render(request, 'dog_profile_view.html',
                          {'dog': this_dog,
                           'image_form': image_form,
                           'image_files': image_files,
                           'this_user': this_user,
                           'num_notifications': num_notifications,
                           'all_trainers': all_trainers,
                           'profile_pic': profile_pic,
                           })

    image_form = MediaForm()
    this_user = ''
    if request.user.is_staff:
        this_user = Trainer.objects.get(admin_user=request.user)
    else:
        this_user = Client.objects.get(user=request.user)
    return render(request, 'dog_profile_view.html',
                  {'dog': this_dog,
                   'image_form': image_form,
                   'image_files': image_files,
                   'this_user': this_user,
                   'num_notifications': num_notifications,
                   'all_trainers': all_trainers,
                   'profile_pic': profile_pic,
                   })


def delete_dog_media_view(request, dogmediafile_id: int):
    this_file = DogMediaFile.objects.get(id=dogmediafile_id)
    this_dog = Dog.objects.get(id=this_file.dog.id)
    user_notifications = Notification.objects.filter(
        send_to=request.user).exclude(seen_by_user=True)
    num_notifications = 0
    for notification in user_notifications:
        num_notifications += 1
    if request.method == "POST":
        this_file.delete()
        return HttpResponseRedirect(reverse('dog_profile_view', args=[this_dog.id]))
    return render(request, 'delete_dog_media.html', {'this_file': this_file, 'this_dog': this_dog, 'num_notifications': num_notifications})


def all_dogs_view(request):
    all_dogs = Dog.objects.all().order_by('name')
    all_profile_pics = DogProfilePic.objects.all()
    this_user = User.objects.get(id=request.user.id)
    all_trainers = Trainer.objects.all()
    user_notifications = Notification.objects.filter(
        send_to=request.user).exclude(seen_by_user=True)
    num_notifications = 0
    for notification in user_notifications:
        num_notifications += 1
    return render(request, 'all_dogs.html', {'dogs': all_dogs, 'this_user': this_user, 'all_trainers': all_trainers, 'num_notifications': num_notifications, 'all_profile_pics': all_profile_pics})


class DogEditView(UpdateView):
    model = Dog
    template_name = 'edit_profile_form.html'
    success_url = '/'
    fields = [
        'name',
        'breed',
        'age_years',
        'age_months',
        'vet_name',
        'vet_number',
        'vet_address',
        'special_needs',
        'extra_notes',
        'no_match_dogs',
    ]

    def get_context_data(self, **kwargs):
        all_trainers = Trainer.objects.all()
        user_notifications = Notification.objects.filter(
            send_to=self.request.user).exclude(seen_by_user=True)
        num_notifications = 0
        for notification in user_notifications:
            num_notifications += 1
        context = super().get_context_data(**kwargs)
        context['all_trainers'] = all_trainers
        context['num_notifications'] = num_notifications
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
