from django.urls import path
from admin_users import views

urlpatterns = [
    path('trainer_form/', views.add_trainer, name='add_trainer'),
    path('trainer_home/<int:user_id>',
         views.trainer_home, name='trainer_home'),
    path('add_admin_user/', views.add_admin_user, name='add_admin_user'),
    path('all_clients/', views.all_clients_view, name='all_clients'),
    path('client_detail/<int:client_id>/',
         views.client_detail_view, name='client_detail'),
    path('my_sessions/<int:user_id>/',
         views.my_sessions_view, name='my_sessions')
]
