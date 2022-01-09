from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAdminUser
)

from rest_framework.decorators import (
    permission_classes,
    api_view
)

from videos.models import (
    Video
)

from playlists.models import PlayList
from playlists.serializers import PlayListSerializer
from videos.serializers import (
    VideoListSerializer
)

@api_view(['GET'])
def AllPlayLists(request):
    qs = PlayList.objects.all()
    serializer = PlayListSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)

@api_view(['GET', 'POST', 'DELETE'])
def PlayListDetail(request, id):
    qs = PlayList.objects.filter(id=id)
    if not qs:
        return Response({"message" : "Playlist not found"}, status=404)
    obj = qs.first()
    if request.method == 'POST' and request.user.is_superuser:
        serializer = PlayListSerializer(instance=obj, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = serializer.data
            return Response(data, status=200)
        return Response({}, status=401)

    if request.method == "DELETE" and request.user.is_superuser:
        obj.delete()
        return Response({"message" : "Playlist successfully deleted"})

    serializer = PlayListSerializer(obj)
    data = serializer.data
    return Response(data, status=200)

@permission_classes([IsAdminUser])
@api_view(['POST'])
def PlayListCreate(request):
    data = request.data
    serializer = PlayListSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        data = serializer.data
        return Response(data, status=201)

    return Response({}, status=401)

@api_view(['POST'])
def AddRemoveVideoToPlayList(request):
    data = request.data
    playlistId = data['playlist_id']
    videoId = data['video_id']
    action = data['action']
    if not playlistId or not videoId:
        return Response({"message" : "No data given"}, status=400)
    playListQS = PlayList.objects.filter(id=playlistId)
    if not playListQS:
        return Response({"message" : "Playlist not found"}, status=404)
    videoQS = Video.objects.filter(id=videoId)
    if not videoQS:
        return Response({"message" : "Video not found"}, status=404)

    videoObj = videoQS.first()
    playlistObj = playListQS.first()
    
    if action == "add":
       playlistObj.videos.add(videoObj)
    elif action == "remove":
       playlistObj.videos.remove(videoObj)
    else:
       return Response({"message" : "Action not valid"}, status=404)   
    return Response({"message" : "Video added to playlist"}, status=200)

@api_view(['GET'])
def GetVideosNotInPlaylist(request, id):
    data = []
    qs = PlayList.objects.filter(id=id)
    if not qs:
        return Response({"message" : "Playlist not found"}, status=404)
    obj = qs.first()
    videosInObj = obj.videos.all()
    videoQs = Video.objects.all()
    for video in videoQs:
        if video not in videosInObj:
            data.append(video)

    serializer = VideoListSerializer(data, many=True)
    return Response(serializer.data, status=200)
