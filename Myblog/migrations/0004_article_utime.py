# Generated by Django 2.2.3 on 2019-08-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myblog', '0003_auto_20190827_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='utime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
