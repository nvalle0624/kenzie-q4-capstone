from django.shortcuts import render

from training_sessions.models import Report, Session, Calendar

from datetime import datetime, date, timedelta

from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
import calendar

# Create your views here


def session_view(request, session_id: int):
    session = Session.objects.get(id=session_id)
    dogs_assigned = []
    for dog in session.dogs_in_session.all():
        dogs_assigned.append(dog)
    return render(request, 'session_detail.html', {'session': session, 'dogs_assigned': dogs_assigned})


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

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)

        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
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
