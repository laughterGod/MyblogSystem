from django.urls import path
from . import views

app_name = 'video'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.VideoDetailView.as_view(), name='detail'),
]