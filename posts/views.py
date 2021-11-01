from typing import List
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView


class PostIndex(ListView):
    pass


class PostSearch(PostIndex):
    pass


class PostCategory(PostIndex):
    pass


class PostShow(UpdateView):
    pass