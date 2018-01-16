from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.timezone import now
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .models import Post, Comment
from .forms import CommentForm, ContactForm

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
            name = strip_tags(form.cleaned_data['name'])
            email = form.cleaned_data['email']
            body = strip_tags(form.cleaned_data['body'])
            post_parent = self.get_object()
            new_comment = Comment(
                name=name,
                email=email,
                body=body,
                post_parent=post_parent
            )
            new_comment.save()
            slug = post_parent.slug
            return HttpResponseRedirect(reverse('post-detail',
                                                kwargs={'slug' : slug}))


class CommentReplyView(DetailView, FormView):
    model = Comment
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = strip_tags(form.cleaned_data['name'])
            email = form.cleaned_data['email']
            body = strip_tags(form.cleaned_data['body'])
            comment_parent = self.get_object()
            new_comment = Comment(
                name=name,
                email=email,
                body=body,
                comment_parent=comment_parent,
            )
            new_comment.save()
            post_parent = comment_parent.post_parent
            slug = post_parent.slug
            return HttpResponseRedirect(reverse('post-detail',
                                                kwargs={'slug' : slug}))

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "blog/contact_me.html"
