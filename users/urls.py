from django.urls import path
from users import views

urlpatterns = [
    path('client_home/',views.client_home, name='client_home' ),
]
