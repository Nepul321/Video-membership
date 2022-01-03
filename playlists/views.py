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