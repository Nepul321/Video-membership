from .views import (
    AddRemoveVideoToPlayList,
    AllPlayLists,
    GetVideosNotInPlaylist,
    PlayListCreate,
    PlayListDetail
)

from django.urls import path

urlpatterns = [
    path('', AllPlayLists, name="all-playlists"),
    path('<int:id>/', PlayListDetail, name="playlist-detail"),
    path('create/', PlayListCreate, name="playlist-create"),
    path('add-video-to-playlist/', AddRemoveVideoToPlayList, name="add-video-to-playlist"),
    path('videos-not-in-playlist/<int:id>/', GetVideosNotInPlaylist, name="videos-not-in-playlist"),
]
