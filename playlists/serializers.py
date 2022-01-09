from inspect import currentframe
from django.db import reset_queries
from rest_framework import serializers
from .models import (
    PlayList
)


class PlayListSerializer(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField(read_only=True)
    thumbnail = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PlayList
        fields = ('id', 'title', 'date', 'videos', 'thumbnail')

    def get_videos(self, obj):
        videos = obj.videos.all()
        results = []
        for video in videos:
            item = {
                "id" : video.id,
                "title" : video.title,
                "thumbnail_image" : video.thumbnail_image.url or None,
                "date" : video.date,
                "views" : video.views
            }
            results.append(item)
        return results

    def get_thumbnail(self, obj):
        videos = obj.videos.all()
        url = "https://images.unsplash.com/photo-1494232410401-ad00d5433cfa?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
        if videos:
            current_obj = videos.first()
            url = current_obj.thumbnail_image.url

        return url 