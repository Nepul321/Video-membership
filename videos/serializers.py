from rest_framework import serializers
from .models import Video

class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'thumbnail_image', 'description', 'date', 'views')

class VideoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'youtube_url', 'thumbnail_image', 'description', 'date', 'views', 'available')

class VideoCreateSerializer(serializers.ModelSerializer):
    is_superuser = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Video
        fields = ('id', 'title', 'youtube_url', 'thumbnail_image', 'description', 'available', 'date', 'views', 'is_superuser')

    def get_is_superuser(self, obj):
        request = self.context['request']
        if request.user.is_superuser:
            return True
        return False