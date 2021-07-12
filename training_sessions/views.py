from django.shortcuts import render
from training_sessions.models import Report

# Create your views here

def reports(request):
    report = Report.objects.all()
    return render(request, 'reports.html', {'report':report})