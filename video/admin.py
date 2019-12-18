from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    # list_display = ('id', 'type_name')
    ordering = ('id',)
