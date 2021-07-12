from django.urls import path
from admin_users import views




urlpatterns = [
    path('trainer_form/',views.add_trainer, name='add_trainer' ),
    path('trainer_profile/',views.trainer_home, name='trainer_home' ),
]
