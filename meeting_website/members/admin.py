from .models import Person
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Preview'
    thumbnail_preview.allow_tags = True


admin.site.register(Person, PostAdmin)
# admin.site.register([Person,PostAdmin])
