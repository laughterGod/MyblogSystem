# Generated by Django 2.2.3 on 2019-08-29 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myblog', '0007_blog_blogtype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['ctime']},
        ),
    ]
