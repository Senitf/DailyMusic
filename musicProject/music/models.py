from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    #exception_many artists in single music
    album_title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
