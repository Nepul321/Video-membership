# Generated by Django 4.0 on 2021-12-30 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='youtube_url',
            field=models.URLField(default='', verbose_name='Youtube URL'),
            preserve_default=False,
        ),
    ]
