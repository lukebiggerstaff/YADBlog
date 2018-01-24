from django.test import Client, TestCase
from django.urls import reverse
from django.core import mail

from blog.models import Comment

from unittest.mock import patch, MagicMock


class TestPostListView(TestCase):
    fixtures = ['blog_views_testdata.json']


    def test_post_list_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEqual(response.template_name, [ 'blog/post_list.html' ])

    def test_list_page_shows_posts_published_before_now(self):
        response = self.client.get('/')
        posts = response.context_data['posts']
        self.assertEqual(posts[0].title, 'post should be visible 1')
        self.assertEqual(posts[1].title, 'post should be visible 2')

    def test_list_page_does_not_show_future_posts(self):
        response = self.client.get('/')
        posts = response.context_data['posts']
        future_post_list = [
            post for post in posts if post.title == 'post should not be visible'
        ]
        self.assertEqual(future_post_list, [])


class TestPostDetailView(TestCase):
    fixtures = ['blog_views_testdata.json']


    def test_post_detail_status_code(self):
        real_post_response = self.client.get('/post-should-be-visible-1')
        self.assertEqual(real_post_response.status_code, 200)
        fake_post_response = self.client.get('/post-is-fake')
        self.assertEqual(fake_post_response.status_code, 404)

    def test_post_detail_uses_correct_template(self):
        response = self.client.get('/post-should-be-visible-1')
        self.assertEqual(response.template_name, ['blog/post_detail.html'])

    @patch('blog.models.Comment.save', MagicMock(name='save'))
    def test_post_detail_comment_works_with_good_data(self):
        response = self.client.post('/post-should-be-visible-1',{
            'name': 'test',
            'email': 'test@test.com',
            'body' : 'test message on test post from test',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/post-should-be-visible-1')
        self.assertTrue(Comment.save.called)
        self.assertEqual(Comment.save.call_count, 1)


class TestCommentReplyView(TestCase):
    fixtures = ['blog_views_testdata.json']
    fixture_comment_id = 12674

    def test_comment_reply_view_status_code(self):
        response = self.client.get(reverse('comment-reply', kwargs={
            'slug' : 'post-should-be-visible-1',
            'pk' : self.fixture_comment_id,
        }))
        self.assertEqual(response.status_code, 200)

    @patch('blog.models.Comment.save', MagicMock(name='save'))
    def test_comment_reply_will_post_with_good_data(self):
        response = self.client.post(
            reverse('comment-reply', kwargs={
                'slug' : 'post-should-be-visible-1',
                'pk' : self.fixture_comment_id
            }), data={
                'name' : 'test',
                'email' : 'test@test.com',
                'body' : 'test message',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/post-should-be-visible-1')
        self.assertTrue(Comment.save.called)
        self.assertEqual(Comment.save.call_count, 1)


class TestContactFormView(TestCase):


    def test_contact_form_view_status_code(self):
        response = self.client.get(reverse('contact-me'))
        self.assertEqual(response.status_code, 200)

    def test_contact_form_view_uses_correct_template(self):
        response = self.client.get(reverse('contact-me'))
        self.assertEqual(response.template_name, [ 'blog/contact_me.html' ])

    def test_contact_form_view_sends_mail_on_post_request(self):
        data = {
            'name' : 'test',
            'email' : 'test@test.com',
            'subject' : 'test subject',
            'message' : 'test message',
        }
        response = self.client.post(
            reverse('contact-me'), data=data
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].body, '{}: {}'.format(data['name'],
                                                              data['message']))
