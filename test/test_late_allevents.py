import unittest

import pytest
from logic.late_allevents_logic import EventFilterPage

class test_all_events(unittest.TestCase):
 @pytest.fixture
 def event_filter_page(driver):
    return EventFilterPage(driver)

 def test_incomplete_events_filter(driver):
    filter_page = event_filter_page(driver)
    filter_page.initiate_filter()
    filter_page.choose_incomplete_events()

 def test_date_based_filter(driver):
    filter_page = event_filter_page(driver)
    filter_page.apply_date_filter()

 def test_event_search(driver):
    filter_page = event_filter_page(driver)
    filter_page.activate_search()
    filter_page.input_search_term("meeting ")


 def test_event_type_filter(driver):
    filter_page = event_filter_page(driver)
    filter_page.apply_type_filter()
