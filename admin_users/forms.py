from django import forms
from django.forms import ModelForm
from admin_users.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = [
            'full_name',
            'phone',
            'cert',
            'field_of_expertise'
        ]
