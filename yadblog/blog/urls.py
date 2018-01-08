from django.urls import path
from . import views

urlpatterns = [
    #path('', views.blog_home, name='blog_home')
    path('', views.PostListView.as_view(), name='post-list'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
]
