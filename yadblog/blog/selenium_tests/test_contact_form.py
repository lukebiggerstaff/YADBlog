import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.core import mail

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
        email_data = {
            'name' : 'test',
            'email' : 'test@test.com',
            'subject' : 'test subject',
            'message' : 'test message',
        }
        name_input = self.browser.find_element_by_id('id_name')
        name_input.send_keys(email_data['name'])

        email_input = self.browser.find_element_by_id('id_email')
        email_input.send_keys(email_data['email'])

        subject_input = self.browser.find_element_by_id('id_subject')
        subject_input.send_keys(email_data['subject'])

        message_input = self.browser.find_element_by_id('id_message')
        message_input.send_keys(email_data['message'])

        submit_button = self.browser.find_element_by_id('id_button')
        submit_button.click()

        self.assertTrue(len(mail.outbox) > 0)
        self.assertEqual(mail.outbox[0].subject, email_data['subject'])
        self.assertEqual(mail.outbox[0].from_email, email_data['email'])
        self.assertTrue(email_data['name'] in mail.outbox[0].body)
