# Generated by Django 3.1.7 on 2021-03-18 06:45

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210317_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=200)),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]
