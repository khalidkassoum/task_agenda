class EventFilterPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input_locator = 'com.claudivan.taskagenda:id/etSearch'
        self.open_filter_options_locator = '(//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/content"])[1]'
        self.incomplete_events_filter_locator = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/title" and @text="Not completed"]'
        self.date_filter_locator = '(//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/content"])[2]'
        self.event_type_filter_locator = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/title" and @text="Type"]'

    def activate_search(self):
        self.driver.find_element_by_id(self.search_input_locator).click()

    def input_search_term(self, term):
        search_field = self.driver.find_element_by_id(self.search_input_locator)
        search_field.clear()
        search_field.send_keys(term)


    def apply_date_filter(self):
        self.driver.find_element_by_xpath(self.date_filter_locator).click()

    def apply_type_filter(self):
        self.driver.find_element_by_xpath(self.event_type_filter_locator).click()

    def initiate_filter(self):
        self.driver.find_element_by_xpath(self.open_filter_options_locator).click()

    def choose_incomplete_events(self):
        self.driver.find_element_by_xpath(self.incomplete_events_filter_locator).click()


