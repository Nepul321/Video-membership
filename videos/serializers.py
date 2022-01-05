from rest_framework import serializers
from .models import Video

class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'thumbnail_image', 'description', 'date', 'views')

class VideoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'youtube_url', 'thumbnail_image', 'description', 'date', 'views')

class VideoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'youtube_url', 'thumbnail_image', 'description')