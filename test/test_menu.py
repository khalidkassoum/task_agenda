import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from infra.task_agenda_app import DriverManager  # Assuming infra contains a setup for initializing driver
from logic.menu_logic import NavigationPage

class NavigationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverManager().initialize_driver()
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_event_overview_navigation(self):
        navigation_page = NavigationPage(self.driver)
        navigation_page.navigate_to_events_overview()
        self.assertTrue(self.wait.until(EC.presence_of_element_located(
            (By.XPATH, navigation_page.view_all_events_selector))))

    def test_delayed_events_navigation(self):
        navigation_page = NavigationPage(self.driver)
        navigation_page.navigate_to_overdue_events()
        self.assertTrue(self.wait.until(EC.presence_of_element_located(
            (By.ID, navigation_page.view_delayed_events_selector))))

    def test_preferences_navigation(self):
        navigation_page = NavigationPage(self.driver)
        navigation_page.navigate_to_preferences()
        self.assertTrue(self.wait.until(EC.presence_of_element_located(
            (By.ID, navigation_page.access_settings_selector))))

    def test_event_colors_and_types_navigation(self):
        navigation_page = NavigationPage(self.driver)
        navigation_page.navigate_to_event_colors_and_types()
        self.assertTrue(self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//path_to_specific_element_for_colors_and_events'))))



    def test_about_page_navigation(self):
        navigation_page = NavigationPage(self.driver)
        navigation_page.navigate_to_about_page()
        self.assertTrue(self.wait.until(EC.presence_of_element_located(
            (By.ID, navigation_page.visit_about_section_selector))))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


