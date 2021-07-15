from django.forms import ModelForm, widgets
from django import forms
from training_sessions.models import Session


class DateInput(forms.DateInput):
    input_type = 'date'


class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = [
            'trainer',
            'activity_name',
            'description',
            'dogs_in_session',
            'date',
            'start_time',
            'end_time',
            'completed',
            'max_slots',
            'notes',
        ]

        widgets = {
            'date': DateInput(),
        }
