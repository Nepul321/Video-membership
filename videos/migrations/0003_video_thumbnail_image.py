# Generated by Django 4.0 on 2021-12-30 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_remove_video_url_video_youtube_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]
