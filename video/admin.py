from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cover', 'file', 'status', 'view_count', 'create_time')
    ordering = ('id',)
