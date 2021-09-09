from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from dogs.models import Dog
from admin_users.models import Trainer

# calendar: https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html

# Create your models here.
from datetime import datetime, time, timedelta
from calendar import HTMLCalendar


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, sessions):
        sessions_per_day = sessions.filter(date__day=day)
        d = ''
        for session in sessions_per_day:
            # each session added links to session view
            time_format = session.start_time.strftime('%I:%M:%p')
            d += f'<li> <a style="color:#f9e54e;text-shadow: 1px 1px #ff0000;text-decoration: underline;" href="/session/{session.id}">{session.activity_name}: {time_format}</a> </li>'

        if day != 0:
            return f"<td style='background-color: #5bbdc8; color:#f9e54e;text-shadow: 2px 2px #ff0000;'><span class='date'>{day}</span><ul> {d} </ul></td>"
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
            date__year=self.year, date__month=self.month)

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
    dogs_in_session = models.ManyToManyField(Dog, blank=True)
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    start_check = models.BooleanField(default=False)
    started = models.TimeField(default=timezone.now)
    ended = models.TimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    report_submitted = models.BooleanField(default=False)
    max_slots = models.IntegerField(default=0)
    slots_available = models.IntegerField(default=0, editable=False)
    full = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    # slot_price = models.IntegerField(blank=True, null=True)
    adjusted_slot_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.activity_name


class Report(models.Model):
    dog_name = models.ForeignKey(Dog, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    time_created = models.DateTimeField(default=timezone.now)
    notes = models.TextField()

    def __str__(self):
        return self.dog_name.name
