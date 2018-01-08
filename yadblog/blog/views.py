from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.timezone import now

from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.filter(published_date__lte=now())
    context_object_name = 'posts'


class PostDetailView(DetailView, FormView):
    model = Post
    context_object_name = 'post'
    form_class = CommentForm
    success_url = reverse_lazy('post-detail')

