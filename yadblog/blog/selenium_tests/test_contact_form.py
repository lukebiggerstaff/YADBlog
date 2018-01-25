import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestContactFormPage(StaticLiveServerTestCase):
    fixtures = ['blog_views_testdata.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_menu_button_goes_to_contact_form_page(self):
        self.browser.get(self.live_server_url)
        menu_button = self.browser.find_element_by_id('navMenuButton')
        menu_button.click()
        contact_form_link = self.browser.find_element_by_class_name('fa-envelope')
        contact_form_link.click()
        current_page = self.browser.current_url
        url_should_be = self.live_server_url + '/contact/'
        self.assertEqual(url_should_be, current_page)

    def test_contact_form_view_has_form(self):
        self.browser.get(self.live_server_url + '/contact/')
        time.sleep(4)



