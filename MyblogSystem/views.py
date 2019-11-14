from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import get_seven_days_read_data
from Myblog.models.BlogModels import Blog


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)
    context = dict()
    context['dates'] = dates
    context['read_nums'] = read_nums
    return render_to_response('home.html', context)

