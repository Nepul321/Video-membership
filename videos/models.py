from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255)
    youtube_url = models.URLField("Youtube URL")
    description = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    available = models.BooleanField(default=True)