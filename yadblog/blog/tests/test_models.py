import unittest
from unittest import TestCase

from django import template

from blog.models import (Post, Comment,
                         PostImage, PostThumbnailImage)

class TestPostModels(TestCase):


    def test_post_str(self):
        post = Post(title='test title')
        self.assertEqual(str(post), post.title)

    def test_post_body_template_function_returns_template(self):
        post = Post(body='this is a template')
        post_body_template = post.body_template
        self.assertIsInstance(post_body_template, template.Template)


class TestCommentModel(TestCase):


    def test_save_increases_post_num_comments(self):
        p = Post.objects.create()
        self.assertEquals(p.num_comments, 0)
        Comment.objects.create(
            post_parent=p
        )
        self.assertEquals(p.num_comments, 1)
        Comment.objects.create(
            post_parent=p
        )
        self.assertEquals(p.num_comments, 2)

    def test_delete_decreases_post_num_comments(self):
        p = Post.objects.create()
        c1 = Comment.objects.create(
            post_parent=p
        )
        c2 = Comment.objects.create(
            post_parent=p
        )
        self.assertEquals(p.num_comments, 2)
        c1.delete()
        self.assertEquals(p.num_comments, 1)
        c2.delete()
        self.assertEquals(p.num_comments, 0)

    def test_comment_str_method(self):
        c = Comment(name='test', body='test message')
        self.assertTrue(c.name in str(c))
        self.assertTrue(c.body[:10] in str(c))


class TestPostImage(TestCase):


    def test_post_image_str(self):
        p = PostImage(name='test')
        self.assertEqual(p.name, str(p))


class TestPostImage(TestCase):


    def test_post_thumbnail_image_str(self):
        p = PostThumbnailImage(name='test')
        self.assertEqual(p.name, str(p))
