

from django.urls import path
from users import views
urlpatterns = [
    path('client_home/<int:user_id>/', views.client_home, name='client_home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('client_form/', views.client_signup_view, name='clientform'),
    path('all_trainers/', views.all_trainers_view, name='all_trainers'),
    path('trainer_detail/<int:trainer_id>',
         views.trainer_detail_view, name='trainer_detail'),
    path('client_edit/<int:pk>/',
         views.ClientEditView.as_view(), name='client_edit'),
    path('user_edit/<int:pk>/',
         views.UserEditView.as_view(), name='user_edit'),
]
