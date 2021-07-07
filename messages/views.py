from django.shortcuts import render
from messages.models import Message
from messages.forms import MessageForm
from notifications.models import Notification
from django.shortcuts import render, HttpResponseRedirect, reverse


# Create your views here.

def message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_message = Message.objects.create(
                text=data['text'],
                sent_by=request.user,
            )
            new_notification = Notification.objects.create(
                text=data['text'],
                sent_by=request.user,
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = MessageForm()
    return render(request, 'tweet.html', {'form': form})


def tweet_detail_view(request, message_id: int):
    message = Message.objects.get(id=message_id)
    return render(request, 'tweet_detail.html', {'message': message})
