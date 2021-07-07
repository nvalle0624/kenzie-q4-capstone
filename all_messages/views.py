from django.shortcuts import render
from all_messages.models import Message
from all_messages.forms import MessageForm
from notifications.models import Notification
from django.shortcuts import render, HttpResponseRedirect, reverse


# Create your views here.

def message_form_view(request):
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


def message_detail_view(request, message_id: int):
    my_message = Message.objects.get(id=message_id)
    return render(request, 'tweet_detail.html', {'message': my_message})
