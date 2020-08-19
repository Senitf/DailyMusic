from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from .funcs import *

# Create your models here.

class Music(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=50, blank=True)
    artist = models.CharField(max_length=50, blank=True)
    album_title = models.CharField(max_length=50, blank=True)

    image = models.ImageField(upload_to=get_file_path)
    
    video_key_direct = models.CharField(max_length=50, blank=True)
    video_key_link = models.CharField(max_length=50, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    like = models.ManyToManyField(User, related_name='like_post', blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite_post', blank=True)

    def __str__(self):
        return self.title + "_" + self.artist

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('music:detail', args=[self.id])
    