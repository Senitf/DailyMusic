from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MusicUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True)
    profile_image = models.ImageField(upload_to='accounts/profile_images', default='accounts/profile_images/default_image/default.jpeg', height_field=600, width_field=600)