from training_sessions.models import Report, Session
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
from media_files.forms import MediaForm
from media_files.models import UserMediaFile, UserProfilePic
from notifications.models import Notification
from django.views.generic import UpdateView


# Create your views here.
''' add trainer id '''


@staff_member_required
def trainer_home(request, user_id: int):
    if request.user.is_authenticated:
        trainer_notifications = Notification.objects.filter(
            send_to=request.user).exclude(seen_by_user=True)
        num_notifications = 0
        for notification in trainer_notifications:
            num_notifications += 1
        profile_pic = ''
        if UserProfilePic.objects.filter(user=request.user):
            profile_pic = UserProfilePic.objects.get(user=request.user)
        image_files = UserMediaFile.objects.filter(user=request.user)
        trainer = Trainer.objects.get(admin_user=request.user)
        all_trainers = Trainer.objects.all()
        if request.method == 'POST':
            image_form = MediaForm(request.POST, request.FILES)
            if image_form.is_valid():
                data = image_form.cleaned_data
                new_image = UserMediaFile.objects.create(
                    user=request.user,
                    image=data['media'],
                )
        image_form = MediaForm()
        return render(request, 'admin_homepage.html', {'trainer': trainer,
                                                       'all_trainers': all_trainers, 'image_form': image_form,
                                                       'image_files': image_files, 'num_notifications': num_notifications,
                                                       'profile_pic': profile_pic})
    return HttpResponseRedirect(reverse('add_trainer'))


@staff_member_required
def add_admin_user(request):
    this_user = Trainer.objects.get(admin_user=request.user)
    all_trianers = Trainer.objects.all()
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
    return render(request, "clientform.html", {"form": form, "this_user": this_user, 'all_trainers': all_trianers})


@staff_member_required
def add_trainer(request):
    all_trainers = Trainer.objects.all()
    if request.method == "POST":
        form = TrainerForm(request.POST)
        print('Form', form.errors)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            new_trainer = Trainer.objects.create(
                admin_user=request.user,
                full_name=data['full_name'],
                phone=data['phone'],
                email=request.user.email,
                cert=data['cert'],
                field_of_expertise=data['field_of_expertise']
            )

            return HttpResponseRedirect(reverse("trainer_home", args=[new_trainer.id]))
    form = TrainerForm()
    return render(request, "trainer_form.html", {"form": form, 'all_trainers': all_trainers})


@staff_member_required
def all_clients_view(request):
    this_user = User.objects.get(id=request.user.id)
    all_clients = Client.objects.all()
    all_trainers = Trainer.objects.all()
    user_notifications = Notification.objects.filter(
        send_to=request.user).exclude(seen_by_user=True)
    num_notifications = 0
    for notification in user_notifications:
        num_notifications += 1
    return render(request, 'all_clients_view.html', {'all_clients': all_clients, 'this_user': this_user, 'all_trainers': all_trainers, 'num_notifications': num_notifications})


@staff_member_required
def client_detail_view(request, client_id: int):
    this_client = Client.objects.get(id=client_id)
    this_user = User.objects.get(id=request.user.id)
    all_trainers = Trainer.objects.all()
    all_profile_pics = UserProfilePic.objects.all()
    return render(request, 'client_detail.html', {'this_client': this_client, 'this_user': this_user, 'all_trainers': all_trainers, 'all_profile_pics': all_profile_pics})


def my_sessions_view(request, user_id: int):
    this_trainer = Trainer.objects.get(id=user_id)
    my_sessions = Session.objects.filter(trainer=this_trainer).order_by('date')
    all_trainers = Trainer.objects.all()

    user_notifications = Notification.objects.filter(
        send_to=request.user).exclude(seen_by_user=True)
    num_notifications = 0
    for notification in user_notifications:
        num_notifications += 1

    my_reports = []
    for each_session in my_sessions:
        my_report = Report.objects.filter(session=each_session)
        for item in my_report:
            my_reports.append(item)
    print('hello')
    return render(request, 'my_sessions.html', {'my_sessions': my_sessions, 'all_trainers': all_trainers, 'my_reports': my_reports, 'this_trainer': this_trainer, 'num_notifications': num_notifications})


def delete_user_media_view(request, usermediafile_id: int):
    this_file = UserMediaFile.objects.get(id=usermediafile_id)
    this_user = User.objects.get(id=this_file.user.id)
    user_notifications = Notification.objects.filter(
        send_to=request.user).exclude(seen_by_user=True)
    num_notifications = 0
    for notification in user_notifications:
        num_notifications += 1
    if request.method == "POST":
        this_file.delete()
        return HttpResponseRedirect(reverse('trainer_home', args=[request.user.id]))
    return render(request, 'delete_user_media.html', {'this_file': this_file, 'this_user': this_user, 'num_notifications': num_notifications})


class TrainerEditView(UpdateView):
    model = Trainer
    template_name = 'edit_profile_form.html'
    success_url = '/'
    fields = [
        'full_name',
        'phone',
        'cert',
        'field_of_expertise',
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
