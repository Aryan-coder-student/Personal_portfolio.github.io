# Generated by Django 3.1.7 on 2021-03-24 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_discord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_name',
        ),
    ]
