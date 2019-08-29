from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from ..models import BlogModels
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.conf import settings


# Create your views here.
def get_blog_list_common_data(request, blogs_all_list):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # 每each_page_blogs_number篇分页
    page_of_blogs = paginator.get_page(page_num)  # 自动转换为int，出错后自动返回1
    current_page_num = page_of_blogs.number  # 获取真实的当前页码
    # 获取当前页和前后两页的页码
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(
        range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # 获取博客分类对应的博客数量
    blog_types = BlogModels.BlogType.objects.all()
    blog_types_list = []
    for blog_type in blog_types:
        blog_type.blog_count = BlogModels.Blog.objects.filter(blog_type=blog_type).count()
        blog_types_list.append(blog_type)

    # 获取日期归档对应的博客数量
    blog_dates = BlogModels.Blog.objects.dates('ctime', 'month', order='DESC')
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = BlogModels.Blog.objects.filter(ctime__year=blog_date.year, ctime__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = blog_types_list
    context['blog_dates'] = blog_dates_dict
    return context


def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogModels.Blog, pk=blog_id)
    context = {}
    context['blog'] = blog
    context['previous_blog'] = BlogModels.Blog.objects.filter(ctime__gt=blog.ctime).last() # __gt大于
    context['next_blog'] = BlogModels.Blog.objects.filter(ctime__lt=blog.ctime).first() # __lt小于
    return render_to_response("Myblog/blog_detail.html", context)


def blog_list(request):
    # blogs = BlogModels.Blog.objects.all()
    blogs_all_list = BlogModels.Blog.objects.filter(is_deleted=False)  # exclude是不包含，与filter相反
    context = get_blog_list_common_data(request, blogs_all_list)
    return render_to_response("Myblog/blog_list.html", context)


def blogs_with_type(request, blog_type_id):
    # blogs = BlogModels.Blog.objects.all()
    blog_type = get_object_or_404(BlogModels.BlogType, pk=blog_type_id)
    blogs_all_list = BlogModels.Blog.objects.filter(is_deleted=False).filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render_to_response('Myblog/blog_with_type.html', context)


def blogs_with_date(request, year, month):
    # blogs = BlogModels.Blog.objects.all()
    blogs_all_list = BlogModels.Blog.objects.filter(is_deleted=False).filter(ctime__year=year, ctime__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = '%s年%s月' % (year, month)
    return render_to_response('Myblog/blog_with_date.html', context)




