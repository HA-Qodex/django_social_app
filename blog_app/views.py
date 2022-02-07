from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class HomeView(ListView):
    model = PostModel
    template_name = 'posts.html'
    context_object_name = 'posts'
