from django.contrib import admin

from .models import Post, Comment, PostImage, PostThumbnailImage

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostImage)
admin.site.register(PostThumbnailImage)
