# Generated by Django 2.2.7 on 2019-12-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_auto_20191218_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
    ]
