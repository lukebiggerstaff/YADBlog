import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase


class TestHomePage(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_browser_title_is_my_name(self):
        self.browser.get(self.live_server_url)

        self.assertIn('Luke Biggerstaff', self.browser.title)
