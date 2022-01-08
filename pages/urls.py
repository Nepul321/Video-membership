from django.urls import path
from .views import (
    AddVideosToPlayList,
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
    path('playlists/<int:id>/', PlayListView, name="playlist"),
    path('playlists/<int:id>/add-videos/', AddVideosToPlayList, name="add-videos"),
]
