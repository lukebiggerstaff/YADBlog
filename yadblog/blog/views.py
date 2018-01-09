from django.shortcuts import render
from django.http import HttpResponseRedirect
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['body']
            post_parent = self.get_object()
            new_comment = Comment(name=name, email=email, body=body, post_parent=post_parent)
            new_comment.save()
            slug = post_parent.slug
            print("NAME: {}".format(name))
            print("EMAIL: {}".format(email))
            print("BODY: {}".format(body))
            print("SLUG: {}".format(slug))
            return HttpResponseRedirect(slug)

