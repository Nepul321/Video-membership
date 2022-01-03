from django.db import reset_queries
from rest_framework import serializers
from .models import (
    PlayList
)

class PlayListSerializer(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PlayList
        fields = ('title', 'date', 'videos')

    def get_videos(self, obj):
        videos = obj.videos.all()
        results = []
        for video in videos:
            item = {
                "id" : video.id,
                "title" : video.title,
                "thumbnail_image" : video.thumbnail_image or None,
                "date" : video.date,
                "views" : video.views
            }
            results.append(item)
        return results