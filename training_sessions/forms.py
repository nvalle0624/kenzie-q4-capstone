from django.forms import ModelForm
from django import forms
from training_sessions.models import Session


class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = [
            'trainer',
            'activity_name',
            'description',
            'dogs_in_session',
            'start_time',
            'end_time',
            'completed',
            'max_slots',
            'notes',
        ]
