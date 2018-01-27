import os

from selenium import webdriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class BaseSeleniumTest(StaticLiveServerTestCase):
    fixtures = ['blog_views_testdata.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        site_url = os.environ.get('SELENIUM_URL')
        if site_url:
            self.live_server_url = site_url
        print("Tests are running against: {}".format(self.live_server_url))

    def tearDown(self):
        self.browser.quit()

