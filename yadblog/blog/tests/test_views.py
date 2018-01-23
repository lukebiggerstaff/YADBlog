import unittest

from unittest import TestCase

from django.test import Client


class TestPostListView(TestCase):

    def test_list(self):
        c = Client()
        self.assertTrue(False)

