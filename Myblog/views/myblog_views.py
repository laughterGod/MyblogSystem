from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from ..models import ArticleModels
from django.template import loader
from django.http import Http404
from django.urls import reverse


# Create your views here.
def index(request):
    return HttpResponse("Hello World!!")


def article_detail(request, article_id):
    # try:
    #     article = ArticleModels.Article.objects.get(pk=article_id)
    #     #return HttpResponse("<h2>文章标题: %s</h2> <br> 文章内容: %s" % (article.title, article.content))
    #     context = {}
    #     context['article'] = article
    #     return render(request, "Myblog/article_detail.html", context)
    # except ArticleModels.Article.DoesNotExist:
    #     raise Http404("id not exist")

    article = get_object_or_404(ArticleModels.Article, pk=article_id)
    context = {}
    context['article'] = article
    return render_to_response("Myblog/article_detail.html", context)


def article_list(request):
    articles = ArticleModels.Article.objects.all()
    context = {}
    context['articles'] = articles
    return render_to_response("Myblog/article_list.html", context)


