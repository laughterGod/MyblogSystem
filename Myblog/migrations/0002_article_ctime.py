# Generated by Django 2.2.3 on 2019-08-27 07:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 27, 7, 24, 5, 411843, tzinfo=utc)),
        ),
    ]
