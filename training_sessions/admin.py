from django.contrib import admin

# Register your models here.

from training_sessions.models import Session, Report

admin.site.register(Session)
admin.site.register(Report)
