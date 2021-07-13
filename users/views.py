
from django.shortcuts import render, HttpResponseRedirect, reverse

from django.contrib.auth import login, logout, authenticate

from users.forms import LoginForm, SignUpForm, ClientForm

from users.models import Client

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.


def client_home(request, user_id: int):
    if request.user.is_authenticated:

       client = Client.objects.get(id=request.user.id)
       return render(request, 'client_homepage.html', {'client':client})

    return HttpResponseRedirect(reverse('sign_up'))


def login_view(request):
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if user:
                
                login(request, user)

                
                return HttpResponseRedirect(reverse("client_home", args=[request.user.id] ))

    form = LoginForm()
    return render(request, "login.html", {"form": form})


def signup_view(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        print('Form', form.errors)

        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user( 
                username=data["username"],
                email=data['email'],

                password=data["password"])
            
            return HttpResponseRedirect(reverse('clientform'))

    form = SignUpForm()
    
    return render(request, "clientform.html", {"form": form})


@login_required
def client_signup_view(request):
    # this_client = Client.objects.get(id=user_id)
    if request.method == 'POST':
        form = ClientForm(request.POST)
        print('Form', form.errors)

        if form.is_valid():
            data = form.cleaned_data
            user = Client.objects.create(
                user=request.user,
                name=data['name'],
                address=data['address'],
                phone_contact=data['phone_contact'],
            )
            return HttpResponseRedirect(reverse("client_home"))
    form = ClientForm()
    return render(request, 'clientform.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
