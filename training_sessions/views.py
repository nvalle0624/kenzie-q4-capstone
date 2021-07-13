from django.shortcuts import render
from training_sessions.models import Report
from datetime import datetime, date

from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from django.utils import Calendar
# Create your views here

def reports(request):
    report = Report.objects.all()
    return render(request, 'reports.html', {'report':report})



class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'
    #  ^ change template name ^ 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()