# Generated by Django 3.1.7 on 2021-03-17 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='channels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_logo', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('channel_desc', models.CharField(max_length=100)),
            ],
        ),
    ]
