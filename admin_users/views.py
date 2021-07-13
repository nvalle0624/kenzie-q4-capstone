from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from admin_users.models import Trainer
from admin_users.forms import TrainerForm
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


# Create your views here.
''' add trainer id '''


@staff_member_required
def trainer_home(request):
    if request.user.is_authenticated:
        trainer = Trainer.objects.get(id=request.user.id)
        return render(request, 'admin_homepage.html', {'trainer': trainer})
    return HttpResponseRedirect(reverse('add_trainer'))


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

            return HttpResponseRedirect(reverse("homepage"))
    form = TrainerForm()
    return render(request, "trainer_form.html", {"form": form})
