from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type =  models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    # ctime = models.DateTimeField(default=timezone.now())
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='admin')
    is_deleted = models.BooleanField(default=False)
    readed_num = models.IntegerField(default=0)

    # 废弃了，已经在admin.py定制了
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-ctime']




