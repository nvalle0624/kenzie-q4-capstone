from django import forms
from training_sessions.models import Session
from dogs.models import Dog
from django.forms.widgets import Textarea


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.DateInput):
    input_type = 'time'


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
            # 'slot_price',
            'notes',
        ]

        widgets = {
            'date': DateInput(),
            'start_time': TimeInput(),
            'end_time': TimeInput(),
        }


class SessionAddDogForm(forms.Form):
    dogs = forms.ModelMultipleChoiceField(queryset=Dog.objects.all())


class SessionTriggerForm(forms.Form):
    ...


class ReportNotesForm(forms.Form):
    notes = forms.CharField(widget=Textarea)
