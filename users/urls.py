

from django.urls import path
from users import views
urlpatterns = [
    path('signup/',views.signup_view, name='signup' ),
    path('login/',views.login_view, name='login' ),
]