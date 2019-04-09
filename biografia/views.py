from django.shortcuts import render


from django.views.generic import ListView, DetailView
from .models import Biografia

# Create your views here.

class IndexView(ListView):

    template_name = 'index.html'
    model = Biografia

class BiografiaDetailView(DetailView):

    template_name = 'biografia_detail.html'
    model = Biografia

