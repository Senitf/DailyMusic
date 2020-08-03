from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator
from urllib.parse import urlparse
from .models import Music
from .funcs import PlayTrailerOnYoutube

# Create your views here.


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
    template_name_suffix = '_create'
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
            message
            s.warning(request, '수정할 권한이 없다.')
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