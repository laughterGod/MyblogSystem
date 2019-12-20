import os
import sys
from django.shortcuts import render
from django.views import generic

from video.models import Video

home_dir = os.path.join(os.path.split(os.path.realpath(__file__))[0], os.path.pardir)
media_dir = home_dir + '/media/'

sys.path.append(media_dir)


class IndexView(generic.ListView):
    model = Video
    template_name = 'video/index.html'
    context_object_name = 'video_list'


class VideoDetailView(generic.DetailView):
    model = Video
    template_name = 'video/detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object()
        os.system("chmod -R 777 " + media_dir)
        obj.increase_view_count()  # 调用自增函数
        return obj

