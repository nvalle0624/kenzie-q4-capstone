from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse 
from users.models import Client

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.
''' add Client id '''
def client_home(request):
    if request.user.is_authenticated:
       client = Client.objects.all()
       return render(request, 'client_homepage.html', {'client':client})
    return HttpResponseRedirect(reverse('sign_up'))