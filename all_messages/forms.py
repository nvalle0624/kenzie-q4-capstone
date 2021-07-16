from admin_users.models import Trainer
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import Textarea


class TrainerMessageForm(forms.Form):
    text = forms.CharField(widget=Textarea)
    send_to = forms.ModelChoiceField(queryset=User.objects.all())


class ClientMessageForm(forms.Form):
    text = forms.CharField(widget=Textarea)
    send_to = forms.ModelChoiceField(
        queryset=User.objects.all().filter(is_staff=True))


class ClientMessageFilterForm(forms.Form):
    name = forms.ModelChoiceField(
        queryset=User.objects.all().filter(is_staff=True), label="Trainer")


class TrainerMessageFilterForm(forms.Form):
    name = forms.ModelChoiceField(
        queryset=User.objects.all(), label='Trainer/Client')
