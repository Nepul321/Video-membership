from django.urls import path
from .views import (
    HomeView,
    PlayListView,
    VideoView,
    VideosView,
    PlayListsView
)

urlpatterns = [
    path('', HomeView, name="home"),
    path('videos/', VideosView, name="videos"),
    path('playlists/', PlayListsView, name="playlists"),
    path('videos/<int:id>/', VideoView, name="video"),
    path('playlists/<int:id>/', PlayListView, name="playlist")
]
