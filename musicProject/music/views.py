from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'music/src/home.html')

def uploadNewMusic(request):
    return render(request, 'music/src/uploadNewMusic.html')