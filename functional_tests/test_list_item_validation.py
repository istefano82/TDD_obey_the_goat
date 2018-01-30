from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from .base import FunctionalTest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from unittest import skip
import os
import time


class ItemValidationTest(FunctionalTest):

    
    def test_cannot_add_empty_lists_items(self):
        # Edit goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box()

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        # She tries again with some text for the item, which now works
        self.get_item_input_box()
        self.get_item_input_box()
        self.wait_for_row_in_list_table('1: Buy Milk')

        # Perversely, she now decides to submit a second blank list item
        self.get_item_input_box()
         
        # She receives a similar warning on the list page
        self.wait_for(lambda: self.assertEqual(
             self.browser.find_element_by_css_selector('.has-error').text,
             "You can't have an empty list item"
        ))

        # And she can correct it by filling some text in 
        self.get_item_input_box()
        self.get_item_input_box()
        self.wait_for_row_in_list_table('1: Buy Milk')
        self.wait_for_row_in_list_table('2: Make Tea')
        
