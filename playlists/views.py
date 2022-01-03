from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAdminUser
)

from rest_framework.decorators import (
    permission_classes,
    api_view
)

from playlists.models import PlayList
from playlists.serializers import PlayListSerializer

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