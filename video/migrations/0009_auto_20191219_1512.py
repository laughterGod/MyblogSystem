# Generated by Django 2.2.7 on 2019-12-19 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0008_auto_20191219_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100, verbose_name='视频标题'),
        ),
    ]
