from django import forms

from users.models import Client


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):

    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'autocomplete': 'off'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


class ClientForm(forms.Form):
    full_name = forms.CharField(max_length=60)
    address = forms.CharField(max_length=300)
    phone_contact = forms.CharField()

    class Meta:
        model = Client

        fields = ('full_name', 'username', 'email',
                  'password', 'address', 'phone_contact')
