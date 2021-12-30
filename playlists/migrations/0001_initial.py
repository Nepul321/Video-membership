# Generated by Django 4.0 on 2021-12-30 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('videos', '0002_remove_video_url_video_youtube_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('videos', models.ManyToManyField(blank=True, related_name='playlist_videos', to='videos.Video')),
            ],
        ),
    ]
