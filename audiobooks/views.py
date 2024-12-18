from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Audiobook

class AudiobookListView(ListView):
    model = Audiobook
    template_name = 'audiobooks/list.html'
    context_object_name = 'audiobooks'

class AudiobookDetailView(DetailView):
    model = Audiobook
    template_name = 'audiobooks/detail.html'

class AudiobookCreateView(CreateView):
    model = Audiobook
    template_name = 'audiobooks/add.html'
    fields = ['title', 'author', 'narrator', 'duration', 'description']
    success_url = '/'