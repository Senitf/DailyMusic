from django.shortcuts import render
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
import random

# Create your views here.
class List(ListView):
    model = PlayList
    template_name = 'playlist/playlist_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '로그인을 먼저 하세요')
            return HttpResponseRedirect('/accounts/login/')
        return super(List,self).dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = PlayList.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(List, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        if(PlayList.objects.count() >= 3):
            items = random.sample(range(1, PlayList.objects.count() + 1), 3)
            context['label1'] = PlayList.objects.get(pk=items[0])
            context['label2'] = PlayList.objects.get(pk=items[1])
            context['label3'] = PlayList.objects.get(pk=items[2])
        return context

class Like(View):
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

class Create(CreateView):
    model = PlayList
    fields = ['title', 'subtitle', 'image']
    template_name = 'playlist/playlist_create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class Detail(DetailView):
    model = Music
    template_name_suffix = '_detail'