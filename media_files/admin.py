from django.contrib import admin
from media_files.models import DogMediaFile, UserMediaFile
# Register your models here.


admin.site.register(DogMediaFile)
admin.site.register(UserMediaFile)
