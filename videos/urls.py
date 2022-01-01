from django.urls import path
from .views import (
    VideoCreateView,
    VideoDetailView,
    VideosListView
)

urlpatterns = [
    path('', VideosListView, name="videos-list"),
    path('<int:id>/', VideoDetailView, name="video-detail"),
    path('create/', VideoCreateView, name="create"),
]
