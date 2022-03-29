from django.contrib import admin

from .models import Person

admin.site.register([Person])
list_display = ['image_tag']
