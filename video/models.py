from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Classification(models.Model):
    list_display = ("title",)
    title = models.CharField(max_length=100,blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "v_classification"


class Video(models.Model):
    STATUS_CHOICES = (
        ('0', '发布中'),
        ('1', '未发布'),
    )
    title = models.CharField(default="你好懒，连标题都不传~", max_length=100, blank=True, verbose_name="视频标题")
    desc = models.CharField(default="你好懒~", max_length=255, blank=True, verbose_name="视频简介")
    # classification = models.ForeignKey(Classification, on_delete=models.CASCADE, null=True)
    # file = models.FileField(upload_to=settings.VIDEO_DATA, max_length=255)
    # cover = models.ImageField(upload_to=settings.VIDEO_COVER, blank=True, null=True)
    file = models.FileField(max_length=255, verbose_name="视频文件")
    cover = models.ImageField(upload_to=settings.VIDEO_COVER, blank=True, null=True, verbose_name="视频封面")
    status = models.CharField(max_length=1 ,choices=STATUS_CHOICES, blank=True, null=True, verbose_name="发布状态")
    view_count = models.IntegerField(default=0, blank=True, verbose_name="观看次数")
    # liked = models.ManyToManyField(User, blank=True, related_name="liked_videos")
    # collected = models.ManyToManyField(User, blank=True, related_name="collected_videos")
    create_time = models.DateTimeField(auto_now_add=True, blank=True, max_length=20, verbose_name="创建时间")

    def increase_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])

    class Meta:
        ordering = ['-create_time']
        verbose_name = '视频'
        verbose_name_plural = verbose_name

