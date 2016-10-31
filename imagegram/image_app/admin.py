from django.contrib import admin
from image_app.models import Image, Profile, Comment

admin.site.register([Image, Profile, Comment])
# Register your models here.
