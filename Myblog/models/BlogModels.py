from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields import exceptions
from read_statistics.models import ReadNumExpandMethod, ReadDetail
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse


# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=15, verbose_name="类型名称")

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '博客类型'
        verbose_name_plural = verbose_name


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50, verbose_name="标题")
    blog_type =  models.ForeignKey(BlogType, on_delete=models.CASCADE, verbose_name="博客类型")
    content = RichTextUploadingField()
    # ctime = models.DateTimeField(default=timezone.now())
    ctime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    utime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="作者")
    read_details = GenericRelation(ReadDetail)
    is_deleted = models.BooleanField(default=False)
    # read_num = models.IntegerField(default=0)

    def get_url(self):
        return reverse('Myblog:blog_detail', kwargs={'blog_id': self.pk})

    def get_user(self):
        return self.author

    def get_email(self):
        return self.author.email

    # 废弃了，已经在admin.py定制了
    def __str__(self):
        return self.title

    '''
    def get_read_num(self):
        try:
            return self.readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0
    '''

    class Meta:
        ordering = ['-ctime']
        verbose_name = '博客'
        verbose_name_plural = verbose_name


'''
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=False)
    
'''



