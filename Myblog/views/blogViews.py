from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from ..models import BlogModels
from django.template import loader
from django.http import Http404
from django.urls import reverse


# Create your views here.
def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogModels.Blog, pk=blog_id)
    context = {}
    context['blog'] = blog
    return render_to_response("Myblog/blog_detail.html", context)


def blog_list(request):
    page_num = request.GET.get('page',1)
    # blogs = BlogModels.Blog.objects.all()
    blogs_all_list = BlogModels.Blog.objects.filter(is_deleted=False)
    paginator = Paginator(blogs_all_list, 10)
    page_of_blogs = paginator.get_page(page_num) # 自动转换为int，出错后自动返回1
    context = {}
    # context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogModels.BlogType.objects.all()
    return render_to_response("Myblog/blog_list.html", context)


def blogs_with_type(request, blog_type_id):
    blog_type = get_object_or_404(BlogModels.BlogType, pk=blog_type_id)
    context = {}
    context['blogs'] = BlogModels.Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogModels.BlogType.objects.all()
    return render_to_response('Myblog/blog_with_type.html', context)


