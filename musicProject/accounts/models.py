from django.db import models
from django.contrib.auth.models import User
import os
import uuid

# Create your models here.

class MusicUser(models.Model):
    def get_file_path(instance, filename):
        filename = instance.nickname + ".jpeg"
        return os.path.join('accounts/profile_images', filename)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True)
    profile_image = models.ImageField(upload_to=get_file_path, default='default_image/default.jpeg')
