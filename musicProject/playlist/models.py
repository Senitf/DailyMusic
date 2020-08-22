from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from music.models import Music
from .funcs import *

# Create your models here.

class PlayList(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlist_user')
    title = models.CharField(max_length=50, blank=True)
    subtitle = models.CharField(max_length=50, blank=True)

    musics = models.ManyToManyField(Music, related_name='musics', blank=True)
    image = models.ImageField(upload_to=get_file_path)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    like = models.ManyToManyField(User, related_name='like_playlist', blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite_playlist', blank=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        ordering = ['-created']
    
    def get_absolute_url(self):
        return reverse("playlist:detail", args=[self.id])