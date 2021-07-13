from django.urls import path
from training_sessions import views


urlpatterns = [
    path('reports/', views.reports, name='reports'),
    path('calendar/', views.CalendarView.as_view(template_name='calendar.html'), name='calendar'),
]
