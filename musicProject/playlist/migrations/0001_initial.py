# Generated by Django 3.0.8 on 2020-08-22 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import playlist.funcs


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('subtitle', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(upload_to=playlist.funcs.get_file_path)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlist_user', to=settings.AUTH_USER_MODEL)),
                ('favorite', models.ManyToManyField(blank=True, related_name='favorite_playlist', to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(blank=True, related_name='like_playlist', to=settings.AUTH_USER_MODEL)),
                ('musics', models.ManyToManyField(blank=True, related_name='playlist', to='music.Music')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]