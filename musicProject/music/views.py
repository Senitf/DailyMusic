from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator
from urllib.parse import urlparse
from .models import *
from .funcs import PlayTrailerOnYoutube
import random

# Create your views here.

class MusicIndex(TemplateView):
    template_name = 'music/music_index.html'

class MusicList(ListView):
    model = Music
    template_name_suffix = '_list'
    paginate_by = 5

    def get_queryset(self):
        return Music.objects.order_by('-like')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(MusicList, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['count'] = Music.objects.count()
        return context
    

class MusicCreate(CreateView):
    model = Music
    fields = ['title', 'artist', 'album_title', 'image']
    template_name_suffix = '_createMusic'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.video_key_direct = PlayTrailerOnYoutube(form.instance.title, form.instance.artist)
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class MusicUpdate(UpdateView):
    model = Music
    fields = ['title', 'artist', 'album_title', 'image']
    template_name_suffix = '_update'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '수정할 권한이 없다.')
            return HttpResponseRedirect('/')
        else:
            return super(MusicUpdate, self).dispatch(request, *args, **kwargs)

class MusicDelete(DeleteView):
    model = Music
    template_name_suffix = '_delete'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '수정할 권한이 없다.')
            return HttpResponseRedirect('/')
        else:
            return super(MusicDelete, self).dispatch(request, *args, **kwargs)

class MusicDetail(DetailView):
    model = Music
    template_name_suffix = '_detail'

class MusicLike(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'music_id' in kwargs:
                music_id = kwargs['music_id']
                music = Music.objects.get(pk=music_id)
                user = request.user
                if user in music.like.all():
                    music.like.remove(user)
                else:
                    music.like.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)

class MusicFavorite(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'music_id' in kwargs:
                music_id = kwargs['music_id']
                music = Music.objects.get(pk=music_id)
                user = request.user
                if user in music.favorite.all():
                    music.favorite.remove(user)
                else:
                    music.favorite.add(user)
            return HttpResponseRedirect('/')

class MusicLikeList(ListView):
    model = Music
    template_name = 'music/music_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '로그인을 먼저 하세요')
            return HttpResponseRedirect('/accounts/login/')
        return super(MusicLikeList,self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        queryset = user.like_post.all()
        return queryset

class MusicFavoriteList(ListView):
    model = Music
    template_name = 'music/music_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '로그인을 먼저 하세요')
            return HttpResponseRedirect('/accounts/login/')
        return super(MusicFavoriteList,self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        queryset = user.favorite_post.all()
        return queryset

class MusicPlayList(ListView):
    model = PlayList
    template_name = 'music/music_playlist.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '로그인을 먼저 하세요')
            return HttpResponseRedirect('/accounts/login/')
        return super(MusicPlayList,self).dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = PlayList.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(MusicPlayList, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        if(PlayList.objects.count() >= 3):
            items = random.sample(range(1, PlayList.objects.count() + 1), 3)
            context['label1'] = PlayList.objects.get(pk=items[0])
            context['label2'] = PlayList.objects.get(pk=items[1])
            context['label3'] = PlayList.objects.get(pk=items[2])
        return context

class PlayListLike(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'playlist_id' in kwargs:
                playlist_id = kwargs['playlist_id']
                playlist = PlayList.objects.get(pk=playlist_id)
                user = request.user
                if user in playlist.like.all():
                    playlist.like.remove(user)
                else:
                    playlist.like.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)

class PlayListCreate(CreateView):
    model = PlayList
    fields = ['title', 'subtitle', 'image']
    template_name = 'music/music_createPlaylist.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})
