

from django.urls import path
from users import views
urlpatterns = [
    path('client_home/<int:user_id>/', views.client_home, name='client_home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('client_form/', views.client_signup_view, name='clientform')
]
