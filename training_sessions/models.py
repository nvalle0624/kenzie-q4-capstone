from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from dogs.models import Dog
from admin_users.models import Trainer

# calendar: https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html

# Create your models here.
from datetime import datetime, timedelta
from calendar import HTMLCalendar


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, sessions):
        sessions_per_day = sessions.filter(start_time__day=day)
        d = ''
        for session in sessions_per_day:
            # each session added links to session view
            d += f'<li> <a href="/session/{session.id}">{session.activity_name}</a> </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, sessions):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, sessions)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        sessions = Session.objects.filter(
            start_time__year=self.year, start_time__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, sessions)}\n'
        return cal


class Session(models.Model):
    trainer = models.ManyToManyField(Trainer)
    activity_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    dogs_in_session = models.ManyToManyField(Dog)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.activity_name


class Report(models.Model):
    dog_name = models.ForeignKey(Dog, on_delete=CASCADE)

    sessions = models.ManyToManyField(Session)

    time_created = models.DateTimeField(default=timezone.now)
