from django.contrib import admin
from image_app.models import Image, Profile

admin.site.register([Image, Profile])
# Register your models here.
