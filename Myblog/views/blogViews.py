from django.shortcuts import render, render_to_response, get_object_or_404
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
    # blogs = BlogModels.Blog.objects.all()
    blogs = BlogModels.Blog.objects.filter(is_deleted=False)
    context = {}
    context['blogs'] = blogs
    context['blog_types'] = BlogModels.BlogType.objects.all()
    return render_to_response("Myblog/blog_list.html", context)


def blogs_with_type(request, blog_type_id):
    blog_type = get_object_or_404(BlogModels.BlogType, pk=blog_type_id)
    context = {}
    context['blogs'] = BlogModels.Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogModels.BlogType.objects.all()
    return render_to_response('Myblog/blog_with_type.html', context)


