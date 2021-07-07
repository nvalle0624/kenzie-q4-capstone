from django import forms
from django.forms.widgets import Textarea


class MessageForm(forms.Form):
    text = forms.CharField(widget=Textarea)
