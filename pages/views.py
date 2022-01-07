from django.shortcuts import redirect, render
from videos.models import Video
from playlists.models import PlayList
from .forms import (
    VideoCreateForm
)

def HomeView(request):
    template = "pages/home.html"
    context = {

    }

    return render(request, template, context)

def VideosView(request):
    template = "pages/videos/videos.html"
    form = VideoCreateForm()
    context = {
       'form' : form,
    }

    return render(request, template, context)

def PlayListsView(request):
    template = "pages/playlists/playlists.html"
    context = {

    }

    return render(request, template, context)

def VideoView(request, id):
    template = "pages/videos/detail.html"
    qs = Video.objects.filter(id=id)
    if not qs:
        return redirect('videos')
    if not request.user.is_superuser:
        available = qs.filter(available=True)
        if not available:
            return redirect('videos')
        obj = available.first()
        obj.views = obj.views + 1
        obj.save()
    else:
        obj = qs.first()
        
    video_id = obj.youtube_url.replace("https://www.youtube.com/watch?v=", "")
    context = {
        'obj' : obj,
        'video_id' : video_id,
    }

    return render(request, template, context)

def PlayListView(request, id):
    template = "pages/playlists/videos.html"
    qs = PlayList.objects.filter(id=id)
    if not qs:
        return redirect('playlists')
    obj = qs.first()
    videos = obj.videos.filter(available=True)
    context = {
      'obj' : obj,
      'videos' : videos,
    }

    return render(request, template, context)