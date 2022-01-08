from re import T
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes
)
from .serializers import (
    VideoCreateSerializer, 
    VideoDetailSerializer, 
    VideoListSerializer
)
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated
)
from .models import Video

@api_view(['GET'])
def VideosListView(request):
    if not request.user.is_superuser:
        qs = Video.objects.filter(available=True)
    else:
        qs = Video.objects.all()
    serializer = VideoListSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)

@api_view(['GET', 'POST', 'DELETE'])
def VideoDetailView(request, id):
    qs = Video.objects.filter(id=id)
    if not qs.exists():
        return Response({'message' : 'Not found'}, status=404)
    # available = qs.filter(available=True)
    # if not available.exists():
    #     return Response({'message' : 'Is not available'}, status=404)
    obj = qs.first()
    if request.method == "POST" and request.user.is_superuser:
        data = request.data
        serializer = VideoDetailSerializer(instance=obj, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
    if request.method == "DELETE" and request.user.is_superuser:
        obj.delete()
        return Response({"message" : "Video deleted"}, status=200)
    serializer = VideoDetailSerializer(obj)
    data = serializer.data
    return Response(data, status=200)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def VideoCreateView(request):
    context = {'request' : request}
    data = request.data
    serializer = VideoCreateSerializer(data=data, context=context)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)

    return Response({}, status=401)
    