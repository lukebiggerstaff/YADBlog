from django.db import models
from django.utils import timezone
from django.urls import reverse



# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    slug = models.SlugField()

    class Meta:
        ordering = ['-published_date',]

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

class Comment(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post_parent = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    comment_parent = models.ForeignKey(
        'Comment',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['timestamp',]

    def __str__(self):
        return '{}: {}...'.format(self.name, self.body[:10])


class PostImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blog")
    related_post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name


class PostThumbnailImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blog")
    related_post = models.OneToOneField(
        'Post',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name
