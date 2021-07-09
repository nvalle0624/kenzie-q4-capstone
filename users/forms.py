from django import forms

from users.models import Client

from phone_field import PhoneField


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ("username", "password")
    
class ClientForm(forms.Form):
    name = forms.CharField(max_length=60)
    address = forms.CharField(max_length=300)
    phone_contact = PhoneField(blank=True, help_text='Contact Number')
    
    # request.user.email