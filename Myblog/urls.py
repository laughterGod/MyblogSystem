from django.urls import path

from . import views

app_name = 'Myblog'
urlpatterns = [
    path('index/', views.index, name='index'),
]