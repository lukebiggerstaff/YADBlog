import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestHomePage(StaticLiveServerTestCase):
    fixtures = ['blog_views_testdata.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_shows_visible_posts(self):
        pass
