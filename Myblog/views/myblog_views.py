from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from ..models import ArticleModels
from django.template import loader
from django.http import Http404
from django.urls import reverse


# Create your views here.
def index(request):
    return HttpResponse("Hello World!!")
    # latest_question_list = ArticleModels.objects.order_by('-pub_date')[:5]
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return render(request, 'Myblog/index.html', context)



