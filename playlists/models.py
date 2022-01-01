from typing import TypeGuard
from django.db import models
from videos.models import (
    Video
)

class PlayList(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
    videos = models.ManyToManyField(Video, blank=True, related_name="playlist_videos")

    class Meta:
        ordering = ['-datetime']