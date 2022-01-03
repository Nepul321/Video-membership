from .views import (
    AllPlayLists
)

from django.urls import path

urlpatterns = [
    path('', AllPlayLists, name="all-playlists"),
]
