from django import forms
from django.forms.widgets import Textarea


class DogProfileForm(forms.Form):
    name = forms.CharField(max_length=30)
    breed = forms.CharField(max_length=40)
    age_years = forms.IntegerField(min_value=0)
    age_months = forms.IntegerField(min_value=0)
    vet_name = forms.CharField(max_length=30)
    vet_number = forms.CharField()
    vet_address = forms.CharField(max_length=200)
    special_needs = forms.CharField(widget=Textarea)
    extra_notes = forms.CharField(widget=Textarea)
