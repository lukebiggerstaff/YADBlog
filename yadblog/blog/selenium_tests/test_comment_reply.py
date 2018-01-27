from .base import BaseSeleniumTest

class TestDetailPage(BaseSeleniumTest):
    fixtures = ['blog_views_testdata.json']
    parent_comment_id = 12674


    def test_comment_reply_page_comment_form_can_submit(self):
        self.browser.get(self.live_server_url + '/post-should-be-visible-1#comments')
        reply_button = self.browser.find_element_by_css_selector(
            '#comment-'+ str(self.parent_comment_id) + '>a>button'
        )
        reply_button.click()
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
            '.child-comment:last-of-type>h4'
        ).text
        comment_body = self.browser.find_element_by_css_selector(
            '.child-comment:last-of-type>p'
        ).text
        self.assertEquals(reply_data['name'], comment_name)
        self.assertEquals(reply_data['body'], comment_body)
