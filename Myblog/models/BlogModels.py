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
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    blog_type =  models.ForeignKey(BlogType, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    # ctime = models.DateTimeField(default=timezone.now())
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    read_details = GenericRelation(ReadDetail)
    is_deleted = models.BooleanField(default=False)
    # read_num = models.IntegerField(default=0)

    def get_url(self):
        return reverse('Myblog:blog_detail', kwargs={'blog_id': self.pk})

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


'''
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=False)
    
'''



