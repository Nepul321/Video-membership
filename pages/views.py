from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from videos.models import Video
from playlists.models import PlayList
from .forms import (
    PlayListCreateForm,
    VideoCreateForm
)
from django.urls import (
    reverse
)

from authentication.decorators import is_super_user

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
    form = PlayListCreateForm()
    context = {
      'form' : form
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
        if request.user.is_authenticated:
            obj.views = obj.views + 1
            obj.save()
    else:
        obj = qs.first()
        
    video_id = obj.youtube_url.replace("https://www.youtube.com/watch?v=", "")
    form = VideoCreateForm(instance=obj)
    if request.method == "POST":
        form = VideoCreateForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('video', args=(obj.id, )))
    context = {
        'obj' : obj,
        'video_id' : video_id,
        'form' : form
    }

    return render(request, template, context)

def PlayListView(request, id):
    template = "pages/playlists/videos.html"
    qs = PlayList.objects.filter(id=id)
    if not qs:
        return redirect('playlists')
    obj = qs.first()
    if not request.user.is_superuser:
        videos = obj.videos.filter(available=True)
    else:
        videos = obj.videos.all()
    form = PlayListCreateForm(instance=obj)
    context = {
      'obj' : obj,
      'videos' : videos,
      'form' : form,
    }

    return render(request, template, context)

@is_super_user
def AddVideosToPlayList(request, id):
    template = "pages/playlists/add-videos.html"
    qs = PlayList.objects.filter(id=id)
    if not qs:
        return redirect('playlists')
    obj = qs.first()
    context = {
      'obj' : obj,
    }

    return render(request, template, context)