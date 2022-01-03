from .views import (
    AllPlayLists,
    PlayListCreate,
    PlayListDetail
)

from django.urls import path

urlpatterns = [
    path('', AllPlayLists, name="all-playlists"),
    path('<int:id>/', PlayListDetail, name="playlist-detail"),
    path('create/', PlayListCreate, name="playlist-create"),
]
