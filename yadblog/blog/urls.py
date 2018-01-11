from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('<slug:slug>/<int:pk>', views.CommentReplyView.as_view(), name='comment-reply'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
