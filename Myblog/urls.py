from django.urls import path

from . import views

app_name = 'Myblog'
urlpatterns = [
    path('index/', views.index, name='index'),
    # article路由已经不用了，用blog代替
    path('article/<int:article_id>', views.article_detail, name='article_detail'),
    path('article/', views.article_list, name='article_list'),
    path('<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('', views.blog_list, name='blog_list'),
    path('type/<int:blog_type_id>', views.blogs_with_type, name='blogs_with_type'),

]