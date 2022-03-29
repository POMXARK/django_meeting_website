from django.contrib import admin

from .models import Person

admin.site.register([Person])
fields = ['image_tag']
readonly_fields = ['image_tag']
