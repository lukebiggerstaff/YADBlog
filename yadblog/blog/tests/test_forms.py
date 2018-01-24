from unittest import TestCase

from blog.forms import ContactForm, CommentForm


class TestCommentForm(TestCase):


    def test_comment_form_has_required_fields(self):
        form = CommentForm()
        self.assertTrue('name' in form.fields)
        self.assertTrue('email' in form.fields)
        self.assertTrue('body' in form.fields)

    def test_comment_form_is_valid_with_good_information(self):
        form = CommentForm(
            data={
                'name':'test',
                'email': 'test@test.com',
                'body' : 'test body',
            }
        )
        self.assertTrue(form.is_valid())

    def test_comment_form_is_not_valid_with_bad_information(self):
        form = ContactForm(
            data={
                'name':'test',
                'email': 'test@test.com',
            }
        )
        self.assertFalse(form.is_valid())


class TestContactForm(TestCase):


    def test_contact_form_has_required_fields(self):
        form = ContactForm()
        self.assertTrue('name' in form.fields)
        self.assertTrue('email' in form.fields)
        self.assertTrue('subject' in form.fields)
        self.assertTrue('message' in form.fields)

    def test_contact_form_is_valid_with_good_information(self):
        form = ContactForm(
            data={
                'name':'test',
                'email': 'test@test.com',
                'subject': 'test subject',
                'message' : 'test message',
            }
        )
        self.assertTrue(form.is_valid())

    def test_contact_form_is_not_valid_with_bad_information(self):
        form = ContactForm(
            data={
                'name':'test',
                'email': 'test@test.com',
                'message' : 'test message',
            }
        )
        self.assertFalse(form.is_valid())
