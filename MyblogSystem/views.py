import datetime

from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data
from Myblog.models.BlogModels import Blog


def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects.filter(read_details__date__lte=today, read_details__date__gte=date).values('id', 'title').annotate(read_num_sum=Sum('read_details__read_num')).order_by('-read_num_sum')
    return blogs[:7]


def get_30_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=30)
    blogs = Blog.objects.filter(read_details__date__lte=today, read_details__date__gte=date).values('id', 'title').annotate(read_num_sum=Sum('read_details__read_num')).order_by('-read_num_sum')
    return blogs[:7]


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)

    # 获取7天热门博客的缓存数据
    hot_blogs_for_7_days = cache.get('hot_blogs_for_7_days')

    # 获取30天热门博客的缓存数据
    hot_blogs_for_30_days = cache.get('hot_blogs_for_30_days')

    if hot_blogs_for_7_days is None:
        hot_blogs_for_7_days = get_7_days_hot_blogs()
        cache.set('hot_blogs_for_7_days', hot_blogs_for_7_days, 3600)   # 缓存1小时

    if hot_blogs_for_30_days is None:
        hot_blogs_for_30_days = get_30_days_hot_blogs()
        cache.set('hot_blogs_for_30_days', hot_blogs_for_30_days, 3600)   # 缓存1小时

    context = dict()
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = get_today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(blog_content_type)
    context['hot_blogs_for_7_days'] = hot_blogs_for_7_days
    context['hot_blogs_for_30_days'] = hot_blogs_for_30_days

    return render_to_response('home.html', context)

