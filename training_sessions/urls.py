from django.urls import path
from training_sessions import views




urlpatterns = [
    path('reports/',views.reports, name='reports' ),
    
]