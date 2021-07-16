from users.models import Client
from django.contrib.auth.decorators import login_required
from admin_users.models import Trainer
from django.contrib.auth.models import User
from django.shortcuts import render
from all_messages.models import Message
from all_messages.forms import ClientMessageForm, TrainerMessageForm, TrainerMessageFilterForm, ClientMessageFilterForm
from notifications.models import Notification
from django.shortcuts import render, HttpResponseRedirect, reverse


# Create your views here.
# @login_required
def all_messages_view(request, user_id: int):
    this_user = User.objects.get(id=request.user.id)
    all_sent_messages = Message.objects.all().filter(sent_by=this_user)
    all_recieved_messages = Message.objects.all().filter(send_to=this_user)
    all_messages = []
    all_trainers = Trainer.objects.all()

    for item in all_sent_messages:
        all_messages.append(item)
    for item in all_recieved_messages:
        all_messages.append(item)
    all_notifications = Notification.objects.all().filter(
        send_to=this_user).exclude(seen_by_user=True)
    count = 0
    for item in all_notifications:
        count += 1

    user_filter = []

    if request.method == 'GET' and this_user.is_staff == False:
        form = ClientMessageFilterForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            if len(user_filter) > 0:
                user_filter.pop(0)
                user_filter.append(data['name'])
            else:
                user_filter.append(data['name'])
            return render(request, 'all_messages.html', {'all_messages': all_messages,
                                                         'all_notifications': all_notifications,
                                                         'count': count,
                                                         'form': form,
                                                         'all_trainers': all_trainers,
                                                         'user_filter': user_filter[0],
                                                         })
    elif request.method == 'POST' and this_user.is_staff == False:
        form2 = ClientMessageForm(request.POST)
        if form2.is_valid():
            data = form2.cleaned_data
            new_message = Message.objects.create(
                text=data['text'],
                sent_by=this_user,
                send_to=data['send_to']
            )
            new_notification = Notification.objects.create(
                text=data['text'],
                sent_by=this_user,
                send_to=data['send_to']
            )
            return HttpResponseRedirect(reverse('all_messages_view', args=[this_user.id]))

    elif request.method == 'GET' and this_user.is_staff == True:
        form = TrainerMessageFilterForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            if len(user_filter) > 0:
                user_filter.pop(0)
                user_filter.append(data['name'])
            else:
                user_filter.append(data['name'])
            form2 = TrainerMessageForm()
            return render(request, 'all_messages.html', {'all_messages': all_messages,
                                                         'all_notifications': all_notifications,
                                                         'count': count,
                                                         'form': form,
                                                         'all_trainers': all_trainers,
                                                         'user_filter': user_filter[0],
                                                         'form2': form2})
    elif request.method == 'POST' and this_user.is_staff == True:
        form2 = TrainerMessageForm(request.POST)
        if form2.is_valid():
            data = form2.cleaned_data
            new_message = Message.objects.create(
                text=data['text'],
                sent_by=this_user,
                send_to=data['send_to']
            )
            new_notification = Notification.objects.create(
                text=data['text'],
                sent_by=this_user,
                send_to=data['send_to']
            )
            return HttpResponseRedirect(reverse('all_messages_view', args=[this_user.id]))

    if this_user.is_staff != True:
        form = ClientMessageFilterForm()
        form2 = ClientMessageForm()
        return render(request, 'all_messages.html', {'all_messages': all_messages,
                                                     'all_notifications': all_notifications,
                                                     'count': count,
                                                     'all_trainers': all_trainers,
                                                     'form': form,
                                                     'form2': form2})
    else:
        form = TrainerMessageFilterForm()
        form2 = TrainerMessageForm()
        return render(request, 'all_messages.html', {'all_messages': all_messages,
                                                     'all_notifications': all_notifications,
                                                     'count': count,
                                                     'all_trainers': all_trainers,
                                                     'form': form,
                                                     'form2': form2})


# @login_required
def client_message_form_view(request):
    all_trainers = Trainer.objects.all()
    this_user = User.objects.get(id=request.user.id)
    if request.method == 'POST' and this_user.is_staff == False:
        form2 = ClientMessageForm(request.POST)
        if form2.is_valid():
            data = form2.cleaned_data
            new_message = Message.objects.create(
                text=data['text'],
                sent_by=this_user,
                send_to=data['send_to']
            )
            new_notification = Notification.objects.create(
                text=data['text'],
                sent_by=this_user,
                send_to=data['send_to']
            )
            return HttpResponseRedirect(reverse('all_messages_view', args=[this_user.id]))

    elif request.method == 'POST' and this_user.is_staff == True:
        form2 = TrainerMessageForm(request.POST)
        if form2.is_valid():
            data = form2.cleaned_data
            new_message = Message.objects.create(
                text=data['text'],
                sent_by=this_user,
                send_to=data['send_to']
            )
            new_notification = Notification.objects.create(
                text=data['text'],
                sent_by=this_user,
                send_to=data['send_to']
            )
            return HttpResponseRedirect(reverse('all_messages_view', args=[this_user.id]))
    if this_user.is_staff != True:
        this_client = Client.objects.get(user=this_user)
        form2 = ClientMessageForm()
        return render(request, 'all_messages.html', {'form2': form2, 'this_client': this_client, 'all_trainers': all_trainers})
    else:
        this_trainer = Trainer.objects.get(admin_user=this_user)
        form2 = TrainerMessageForm()
        return render(request, 'all_messages.html', {'form2': form2, 'this_trainer': this_trainer, 'all_trainers': all_trainers})
