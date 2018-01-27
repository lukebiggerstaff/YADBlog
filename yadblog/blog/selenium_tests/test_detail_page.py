from .base import BaseSeleniumTest


class TestDetailPage(BaseSeleniumTest):
    fixtures = ['blog_views_testdata.json']


    def submit_comment(self, reply_data):
        name_input = self.browser.find_element_by_id('id_name')
        name_input.send_keys(reply_data['name'])

        email_input = self.browser.find_element_by_id('id_email')
        email_input.send_keys(reply_data['email'])

        body_input = self.browser.find_element_by_id('id_body')
        body_input.send_keys(reply_data['body'])

        reply_button = self.browser.find_element_by_id('id_submit')
        reply_button.click()


    def test_home_page_links_to_detail_page(self):
        self.browser.get(self.live_server_url)

        # grab headline links from post in fixture data
        fixture_link_list = self.browser.find_elements_by_partial_link_text(
            'Post Should'
        )
        post_links = dict()
        for link in fixture_link_list:
            link_text = link.text
            link_url = link.get_attribute('href')
            post_links[link_url] = link_text
        for link in post_links.keys():
            self.browser.get(link)
            headline = self.browser.find_element_by_class_name('main-heading').text
            self.assertEqual(post_links[link], headline)

    def test_detail_page_comment_form_can_submit(self):
        self.browser.get(self.live_server_url + '/post-should-be-visible-1#comments')
        reply_data = {
            'name' : 'selenium user 1',
            'email' : 'test3@test.com',
            'body' : 'selenium comment #1'
        }
        name_input = self.browser.find_element_by_id('id_name')
        name_input.send_keys(reply_data['name'])

        email_input = self.browser.find_element_by_id('id_email')
        email_input.send_keys(reply_data['email'])

        body_input = self.browser.find_element_by_id('id_body')
        body_input.send_keys(reply_data['body'])

        reply_button = self.browser.find_element_by_id('id_submit')
        reply_button.click()

        comment_name = self.browser.find_element_by_css_selector(
            '.parent-comment:last-of-type>h4'
        ).text
        comment_body = self.browser.find_element_by_css_selector(
            '.parent-comment:last-of-type>p'
        ).text
        self.assertEquals(reply_data['name'], comment_name)
        self.assertEquals(reply_data['body'], comment_body)
