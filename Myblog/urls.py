from django.urls import path

from . import views

app_name = 'Myblog'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('article/<int:article_id>', views.article_detail, name='article_detail'),
    path('article/', views.article_list, name='article_list'),
]