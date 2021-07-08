from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse 
from admin_users.models import Trainer
from admin_users.forms import TrainerForm
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def add_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST)
        print('Form', form.errors)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            Trainer.objects.create(
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