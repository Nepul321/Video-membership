from django.shortcuts import render

def HomeView(request):
    template = "pages/home.html"
    context = {

    }

    return render(request, template, context)

def VideosView(request):
    template = "pages/videos/videos.html"
    context = {

    }

    return render(request, template, context)

def PlayListsView(request):
    template = "pages/playlists/playlists.html"
    context = {

    }

    return render(request, template, context)