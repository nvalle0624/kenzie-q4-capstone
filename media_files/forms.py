from django import forms


class MediaForm(forms.Form):
    media = forms.FileField(required=False, label='media')
