from django.shortcuts import render
from django.views import generic

from video.models import Video


class IndexView(generic.ListView):
    model = Video
    template_name = 'video/index.html'
    context_object_name = 'video_list'


class VideoDetailView(generic.DetailView):
    model = Video
    template_name = 'video/detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.increase_view_count()  # 调用自增函数
        return obj

