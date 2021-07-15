from os import name
from django.urls import path
from training_sessions import views


urlpatterns = [
    path('reports/', views.reports, name='reports'),
    path('calendar/', views.CalendarView.as_view(template_name='calendar.html'), name='calendar'),
    path('session/<int:session_id>/', views.session_view, name='session_detail'),
    path('session_form/', views.SessionFormView.as_view(
        template_name='session_form.html'), name='session_form'),
    path('session_edit/<int:pk>/',
         views.SessionEditView.as_view(), name='session_edit'),
    path('session_add_dog/<int:session_id>/',
         views.session_add_dog_view, name='session_add_dog'),
]
