from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('<slug:slug>/<int:pk>', views.CommentReplyView.as_view(), name='comment-reply'),
]
