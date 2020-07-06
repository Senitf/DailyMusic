from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Music
# Create your views here.

def home(request):
    Musics = Music.objects
    return render(request, 'music/src/home.html', {'Musics' : Musics})

def uploadNewMusic(request):
    return render(request, 'music/src/uploadNewMusic.html')

def create(request):
    music = Music()
    music.title = request.GET['title']
    music.artist = request.GET['artist']
    music.album_title = request.GET['album_title']
    music.save
    return redirect('')