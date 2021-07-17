from django.contrib import admin
from media_files.models import DogMediaFile, UserMediaFile, UserProfilePic, DogProfilePic
# Register your models here.


admin.site.register(DogMediaFile)
admin.site.register(UserMediaFile)
admin.site.register(UserProfilePic)
admin.site.register(DogProfilePic)
