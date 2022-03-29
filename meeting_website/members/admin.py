from .models import Person , Post
from django.contrib import admin

admin.site.register([Person])


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


admin.site.register(Post, PostAdmin)
