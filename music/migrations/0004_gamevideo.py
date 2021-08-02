# Generated by Django 3.1.7 on 2021-03-19 12:05

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]