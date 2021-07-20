
from django.shortcuts import render, HttpResponseRedirect, reverse

from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from users.forms import LoginForm, SignUpForm, ClientForm
from django.views.generic import UpdateView
from django import forms
from users.models import Client
from notifications.models import Notification

from django.contrib.auth.models import User
from admin_users.models import Trainer
from media_files.models import UserMediaFile, UserProfilePic

from django.contrib.auth.decorators import login_required

# Create your views here.


def err_404(request, *args, **kwargs):

    return render(request, 'generic_err.html', {})


def err_500(request, *args, **kwargs):

    return render(request, 'generic_err.html', {})


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
        profile_pic = ''
        if UserProfilePic.objects.filter(user=request.user):
            profile_pic = UserProfilePic.objects.get(user=request.user)
        client = Client.objects.get(user=request.user)
        client_notifications = Notification.objects.filter(
            send_to=request.user).exclude(seen_by_user=True)
        num_notifications = 0
        for notification in client_notifications:
            num_notifications += 1
        all_trainers = Trainer.objects.all()
        return render(request, 'client_homepage.html', {'client': client,
                                                        'client_notifications': client_notifications,
                                                        'num_notifications': num_notifications,
                                                        'all_trainers': all_trainers,
                                                        'profile_pic': profile_pic})
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
    all_trainers = Trainer.objects.all().order_by('full_name')
    all_profile_pics = UserProfilePic.objects.all()
    this_user = User.objects.get(id=request.user.id)
    user_notifications = Notification.objects.filter(
        send_to=request.user).exclude(seen_by_user=True)
    num_notifications = 0
    for notification in user_notifications:
        num_notifications += 1
    return render(request, 'all_trainers.html', {'all_trainers': all_trainers, 'this_user': this_user, 'num_notifications': num_notifications, 'all_profile_pics': all_profile_pics})


def trainer_detail_view(request, trainer_id: int):
    this_trainer = Trainer.objects.get(id=trainer_id)
    all_profile_pics = UserProfilePic.objects.all()
    this_user = User.objects.get(id=request.user.id)
    all_trainers = Trainer.objects.all()
    user_notifications = Notification.objects.filter(
        send_to=request.user).exclude(seen_by_user=True)
    num_notifications = 0
    for notification in user_notifications:
        num_notifications += 1
    return render(request, 'trainer_detail.html', {'this_trainer': this_trainer,
                                                   'this_user': this_user, 'all_trainers': all_trainers,
                                                   'num_notifications': num_notifications, 'all_profile_pics': all_profile_pics})


class ClientEditView(UpdateView):
    model = Client
    # form_class = ClientForm

    template_name = 'edit_profile_form.html'
    success_url = '/'
    fields = [
        'full_name',
        'address',
        'phone_contact'
    ]

    def get_context_data(self, **kwargs):
        all_trainers = Trainer.objects.all()
        user_notifications = Notification.objects.filter(
            send_to=self.request.user).exclude(seen_by_user=True)
        num_notifications = 0
        for notification in user_notifications:
            num_notifications += 1
        context = super().get_context_data(**kwargs)
        context['all_trainers'] = all_trainers
        context['num_notifications'] = num_notifications
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserEditView(UpdateView):
    model = User
    template_name = 'edit_profile_form.html'
    fields = [
        'username',
        'email',
    ]

    def get_success_url(self):
        if self.get_object().is_staff:
            return f'/trainer_home/{self.get_object().id}'
        else:
            return f'/client_home/{self.get_object().id}'

    def get_context_data(self, **kwargs):
        all_trainers = Trainer.objects.all()
        user_notifications = Notification.objects.filter(
            send_to=self.request.user).exclude(seen_by_user=True)
        num_notifications = 0
        for notification in user_notifications:
            num_notifications += 1
        context = super().get_context_data(**kwargs)
        context['all_trainers'] = all_trainers
        context['num_notifications'] = num_notifications
        return context

    def form_valid(self, form):
        form.save()
        if self.get_object().is_staff:
            this_trainer = Trainer.objects.get(
                admin_user=self.get_object())
            data = form.cleaned_data
            this_trainer.email = data['email']
            this_trainer.save()
        else:
            this_client = Client.objects.get(user=self.get_object())
            data = form.cleaned_data
            this_client.email = data['email']
            this_client.save()
        return super().form_valid(form)
