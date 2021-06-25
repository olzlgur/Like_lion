from typing import List
from django.shortcuts import render
from .models import Bookmark
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView


class BookmarkListView(ListView):
  model = Bookmark

class BookmarkCreateView(CreateView):
  model = Bookmark
  fields = ['site_name', 'url']
  success_url = reverse_lazy('list')
  template_name_suffix = "_create"

class BookmarkDetailView(DetailView):
  model = Bookmark
