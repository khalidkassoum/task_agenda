from appium import webdriver

class DriverManager:
    def initialize_driver(self):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "12.0",
            "deviceName": "emulator-5554",
            "appPackage": "com.claudivan.taskagenda",
            "appActivity": "com.android.Activities.MainActivity",
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
        return driver

    def tear_down(driver):
        driver.quit()

    