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

class Index(TemplateView):
    template_name = 'music/music_index.html'

class List(ListView):
    model = Music
    template_name_suffix = '_list'
    paginate_by = 5

    def get_queryset(self):
        return Music.objects.order_by('-like')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(List, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['count'] = Music.objects.count()
        return context
    

class Create(CreateView):
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

class Update(UpdateView):
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
            return super(Update, self).dispatch(request, *args, **kwargs)

class Delete(DeleteView):
    model = Music
    template_name_suffix = '_delete'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '수정할 권한이 없다.')
            return HttpResponseRedirect('/')
        else:
            return super(Delete, self).dispatch(request, *args, **kwargs)

class Detail(DetailView):
    model = Music
    template_name_suffix = '_detail'

class Like(View):
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

class Favorite(View):
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

class Likelist(ListView):
    model = Music
    template_name = 'music/music_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '로그인을 먼저 하세요')
            return HttpResponseRedirect('/accounts/login/')
        return super(Likelist,self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        queryset = user.like_post.all()
        return queryset

class Favoritelist(ListView):
    model = Music
    template_name = 'music/music_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '로그인을 먼저 하세요')
            return HttpResponseRedirect('/accounts/login/')
        return super(Favoritelist,self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        queryset = user.favorite_post.all()
        return queryset