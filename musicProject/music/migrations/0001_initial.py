# Generated by Django 3.0.8 on 2020-08-26 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import music.funcs


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('artist', models.CharField(blank=True, max_length=50)),
                ('album_title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(upload_to=music.funcs.get_file_path)),
                ('video_key_direct', models.CharField(blank=True, max_length=50)),
                ('video_key_link', models.CharField(blank=True, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('favorite', models.ManyToManyField(blank=True, related_name='favorite_post', to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(blank=True, related_name='like_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
