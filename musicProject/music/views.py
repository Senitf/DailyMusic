from django.shortcuts import render
from .models import Music
# Create your views here.

def home(request):
    Musics = Music.objects
    return render(request, 'music/src/home.html', {'Musics' : Musics})

def uploadNewMusic(request):
    return render(request, 'music/src/uploadNewMusic.html')