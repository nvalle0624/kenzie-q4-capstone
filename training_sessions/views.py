from dogs.models import Dog
from django.contrib.auth.models import User
from admin_users.models import Trainer
from users.models import Client
from training_sessions.forms import SessionAddDogForm, SessionForm, DateInput, TimeInput
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic.edit import FormView
from django.views.generic import UpdateView
from training_sessions.models import Report, Session, Calendar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.forms.models import modelform_factory

from datetime import datetime, date, timedelta

from django.http import HttpResponse, request
from django.views import generic
from django.utils.safestring import mark_safe
import calendar

# Create your views here


def session_view(request, session_id: int):
    this_user = User.objects.get(id=request.user.id)
    session = Session.objects.get(id=session_id)
    dogs_in_session = session.dogs_in_session.all()
    dogs_assigned = []

    for dog in dogs_in_session:
        dogs_assigned.append(dog)
    # this is for demo purposes. ideally, there would be different types of sessions with different limits
    if len(dogs_assigned) >= session.max_slots:
        session.full = True
        print('session is full')
    else:
        session.full = False
    if session.completed:
        for dog in dogs_assigned:
            new_report = Report.objects.create(
                dog_name=dog,
                time_created=session.end_time,
            )
    num_of_dogs = len(dogs_assigned)
    open_slots = session.max_slots - num_of_dogs
    session.slots_available = open_slots
    session.save()
    return render(request, 'session_detail.html', {'session': session, 'dogs_assigned': dogs_assigned, 'this_user': this_user, 'num_of_dogs': num_of_dogs, 'open_slots': open_slots})


def reports(request):
    report = Report.objects.all()
    return render(request, 'reports.html', {'report': report})

# calendar: https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html


class CalendarView(generic.ListView):
    model = Session
    template_name = 'calendar.html'
    #  ^ change template name ^

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))
        d = get_date(self.request.GET.get('month', None))
        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        if self.request.user.is_staff:
            this_user = Trainer.objects.get(admin_user=self.request.user)
        else:
            this_user = Client.objects.get(user=self.request.user)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)

        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['this_user'] = this_user
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


class SessionFormView(UserPassesTestMixin, FormView):

    template_name = 'session_form.html'
    form_class = SessionForm
    success_url = '/calendar/'

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# editability from: https://www.youtube.com/watch?v=J7xaESAddDQ&list=RDCMUCFB0dxMudkws1q8w5NJEAmw&index=1


class SessionEditView(UserPassesTestMixin, UpdateView):
    model = Session
    form_class = SessionForm
    template_name = 'session_edit.html'
    success_url = '/calendar/'

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def session_add_dog_view(request, session_id: int):
    this_client = Client.objects.get(user=request.user)
    this_session = Session.objects.get(id=session_id)
    if request.method == 'POST':
        form = SessionAddDogForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            dogs = data['dogs']

            for dog in dogs:
                if len(dogs) <= this_session.slots_available:
                    this_session.dogs_in_session.add(dog)
                    this_session.save()
                else:
                    slots_full_message = "Sorry! This session doesn't have enough space."
                    form = SessionAddDogForm()
                    form.fields['dogs'].queryset = Dog.objects.filter(
                        owner=this_client)
                    return render(request, 'session_add_dog_form.html', {'form': form, 'this_session': this_session, 'slots_full_message': slots_full_message})
            return HttpResponseRedirect(reverse('session_detail', args=[this_session.id]))
    form = SessionAddDogForm()
    form.fields['dogs'].queryset = Dog.objects.filter(owner=this_client)
    return render(request, 'session_add_dog_form.html', {'form': form, 'this_session': this_session})
