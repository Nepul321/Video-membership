from django.shortcuts import render

def HomeView(request):
    template = "pages/home.html"
    context = {

    }

    return render(request, template, context)