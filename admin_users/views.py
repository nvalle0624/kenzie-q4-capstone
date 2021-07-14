from users.models import Client
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from admin_users.models import Trainer
from dogs.models import Dog
from admin_users.forms import TrainerForm
from django.contrib.auth.models import User
from users.forms import SignUpForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.
''' add trainer id '''


@staff_member_required
def trainer_home(request, user_id: int):
    if request.user.is_authenticated:
        trainer = Trainer.objects.get(admin_user=request.user)
        return render(request, 'admin_homepage.html', {'trainer': trainer})
    return HttpResponseRedirect(reverse('add_trainer'))


@staff_member_required
def add_admin_user(request):
    this_user = Trainer.objects.get(admin_user=request.user)
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print('Form', form.errors)
        if form.is_valid():
            data = form.cleaned_data
            new_admin_user = User.objects.create_user(
                username=data["username"],
                email=data['email'],
                password=data["password"],
                is_staff=True)
            return HttpResponseRedirect(reverse('login'))
    form = SignUpForm()
    return render(request, "clientform.html", {"form": form, "this_user": this_user})


@staff_member_required
def add_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST)
        print('Form', form.errors)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            new_trainer = Trainer.objects.create(
                admin_user=data['admin_user'],
                name=data['name'],
                phone=data['phone'],
                email=data['email'],
                cert=data['cert'],
                field_of_expertise=data['field_of_expertise']

            )

            return HttpResponseRedirect(reverse("trainer_home", args=[new_trainer.id]))
    form = TrainerForm()
    return render(request, "trainer_form.html", {"form": form})


@staff_member_required
def all_clients_view(request):
    this_user = User.objects.get(id=request.user.id)
    all_clients = Client.objects.all()
    return render(request, 'all_clients_view.html', {'all_clients': all_clients, 'this_user': this_user})


@staff_member_required
def client_detail_view(request, client_id: int):
    this_client = Client.objects.get(id=client_id)
    this_user = User.objects.get(id=request.user.id)
    return render(request, 'client_detail.html', {'this_client': this_client, 'this_user': this_user})
