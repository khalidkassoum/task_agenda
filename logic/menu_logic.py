class NavigationPage:
    def __init__(self, driver):
        self.driver = driver
        self.view_all_events_selector = '//android.widget.TextView[@text="All events"]'
        self.view_delayed_events_selector = 'com.claudivan.taskagenda:id/tvEventosAtrasados'
        self.explore_colors_and_types_selector = '//android.widget.TextView[@text="Colors and event types"]'
        self.visit_about_section_selector = 'com.claudivan.taskagenda:id/btSobre'
        self.access_settings_selector = 'com.claudivan.taskagenda:id/btAjustes'


    def navigate_to_events_overview(self):
        self.driver.find_element_by_xpath(self.view_all_events_selector).click()

    def navigate_to_preferences(self):
        self.driver.find_element_by_id(self.access_settings_selector).click()

    def navigate_to_event_colors_and_types(self):
        self.driver.find_element_by_xpath(self.explore_colors_and_types_selector).click()

    def navigate_to_about_page(self):
        self.driver.find_element_by_id(self.visit_about_section_selector).click()

    def navigate_to_overdue_events(self):
        self.driver.find_element_by_id(self.view_delayed_events_selector).click()


