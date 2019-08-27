from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author' ,'ctime', 'utime')
    ordering = ('-id',)


#admin.site.register(Article, ArticleAdmin)