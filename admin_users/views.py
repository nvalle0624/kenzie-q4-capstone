from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from admin_users.models import Trainer
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
    return render(request, "clientform.html", {"form": form})


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
