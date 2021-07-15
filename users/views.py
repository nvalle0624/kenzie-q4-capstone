
from django.shortcuts import render, HttpResponseRedirect, reverse

from django.contrib.auth import login, logout, authenticate

from users.forms import LoginForm, SignUpForm, ClientForm

from users.models import Client

from django.contrib.auth.models import User
from admin_users.models import Trainer

from django.contrib.auth.decorators import login_required

# Create your views here.


def app_home(request):
    if request.user.is_authenticated and request.user.is_staff:
        this_user = Trainer.objects.get(admin_user=request.user)
        return render(request, 'app_home.html', {'this_user': this_user})
    elif request.user.is_authenticated and not request.user.is_staff:
        this_user = Client.objects.get(user=request.user)
        return render(request, 'app_home.html', {'this_user': this_user})
    return render(request, 'app_home.html')


def client_home(request, user_id: int):
    if request.user.is_authenticated:
        client = Client.objects.get(user=request.user)
        return render(request, 'client_homepage.html', {'client': client})
    return HttpResponseRedirect(reverse('sign_up'))


def login_view(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )

            login(request, user)
            if user.is_staff == True:
                if Trainer.objects.filter(admin_user=request.user).exists():
                    this_trainer = Trainer.objects.get(admin_user=request.user)
                    return HttpResponseRedirect(reverse("trainer_home", args=[this_trainer.id]))
                else:
                    return HttpResponseRedirect(reverse("add_trainer"))
            else:
                if Client.objects.filter(user=request.user).exists():
                    this_client = Client.objects.get(user=request.user)
                    return HttpResponseRedirect(reverse("client_home", args=[this_client.id]))
                else:
                    return HttpResponseRedirect(reverse("clientform"))

    form = LoginForm()
    if request.user.is_authenticated and request.user.is_staff:
        this_user = Trainer.objects.get(admin_user=request.user)
        return render(request, 'login.html', {'form': form, 'this_user': this_user})
    elif request.user.is_authenticated and not request.user.is_staff:
        this_user = Client.objects.get(user=request.user)
        return render(request, 'login.html', {'form': form, 'this_user': this_user})
    else:
        return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("app_home"))


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
            # login(request, new_user)
            return HttpResponseRedirect(reverse('login'))

    form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def client_signup_view(request):
    this_client = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = ClientForm(request.POST)
        print('Form', form.errors)

        if form.is_valid():
            data = form.cleaned_data
            my_user = Client.objects.create(
                user=request.user,
                full_name=data['full_name'],
                address=data['address'],
                phone_contact=data['phone_contact'],
                email=request.user.email
            )
            return HttpResponseRedirect(reverse("client_home", args=[this_client.id]))
    form = ClientForm()
    return render(request, 'clientform.html', {'form': form})


def all_trainers_view(request):
    all_trainers = Trainer.objects.all()
    this_user = User.objects.get(id=request.user.id)
    return render(request, 'all_trainers.html', {'all_trainers': all_trainers, 'this_user': this_user})


def trainer_detail_view(request, trainer_id: int):
    this_trainer = Trainer.objects.get(id=trainer_id)
    this_user = User.objects.get(id=request.user.id)
    return render(request, 'trainer_detail.html', {'this_trainer': this_trainer, 'this_user': this_user})
