from .base import BaseSeleniumTest

from selenium.common.exceptions import NoSuchElementException


class TestHomePage(BaseSeleniumTest):
    fixtures = ['blog_views_testdata.json']


    def test_home_page_shows_visible_posts(self):
        self.browser.get(self.live_server_url)
        headlines_list = self.browser.find_elements_by_partial_link_text('Post Should Be Visible')
        self.assertEqual(headlines_list[0].text, 'Post Should Be Visible 1')
        self.assertEqual(headlines_list[1].text, 'Post Should Be Visible 2')

    def test_home_page_menu_button_works(self):
        self.browser.get(self.live_server_url)
        menu_button = self.browser.find_element_by_id('navMenuButton')
        menu_button.click()
        menu_slider_onscreen = self.browser.find_element_by_class_name('onscreen')
        self.assertTrue(menu_slider_onscreen)
        menu_button.click()
        try:
            menu_slider_offscreen = self.browser.find_element_by_class_name('onscreen')
        except NoSuchElementException as e:
            menu_slider_offscreen = False
        self.assertFalse(menu_slider_offscreen)

