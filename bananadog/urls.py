"""bananadog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin


from dogs import views as dog_views
from all_messages import views as message_views
from notifications import views as notifications_view
from users import views as user_views

from django.urls import path, include


urlpatterns = [
    path('', user_views.app_home, name='app_home'),
    path('', include('admin_users.urls')),
    path('', include('users.urls')),
    path('', include('training_sessions.urls')),
    path('admin/', admin.site.urls),
    path('dog_form/', dog_views.dog_profile_form_view, name='dog_form_view'),
    path('all_dogs/', dog_views.all_dogs_view, name="all_dogs_view"),
    path('dog_profile/<int:dog_id>/',
         dog_views.dog_profile_view, name='dog_profile_view'),
    path('delete_dog_media/<int:dogmediafile_id>/',
         dog_views.delete_dog_media_view, name='delete_dog_media_view'),
    path('message_form/', message_views.client_message_form_view,
         name='message_form_view'),
    path('all_messages/<int:user_id>/', message_views.all_messages_view,
         name='all_messages_view'),
    path('notifications/<int:user_id>/',
         notifications_view.notifications_view, name='notifications_view')
]
