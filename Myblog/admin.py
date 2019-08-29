from django.contrib import admin
from .models import Article, Blog, BlogType


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author' ,'ctime', 'utime', 'is_deleted')
    ordering = ('-id',)


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    ordering = ('id',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_type', 'author', 'readed_num', 'ctime', 'utime', 'is_deleted')
    ordering = ('-id',)


# admin.site.register(Article, ArticleAdmin)

