from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # ctime = models.DateTimeField(default=timezone.now())
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    is_deleted = models.BooleanField(default=False)
    readed_num = models.IntegerField(default=0)

    # 废弃了，已经在admin.py定制了
    def __str__(self):
        return self.title

