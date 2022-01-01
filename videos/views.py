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
    qs = Video.objects.filter(available=True)
    serializer = VideoListSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)

@api_view(['GET'])
def VideoDetailView(request, id):
    qs = Video.objects.filter(id=id)
    available = qs.filter(available=True)
    obj = available.first()
    serializer = VideoDetailSerializer(obj)
    data = serializer.data
    return Response(data, status=200)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def VideoCreateView(request):
    data = request.data
    serializer = VideoCreateSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)

    return Response({}, status=401)
    