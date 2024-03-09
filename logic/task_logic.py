from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class EventScheduler:
    def __init__(self, driver):
        self.driver = driver
        self.addButtonID = 'com.claudivan.taskagenda:id/btNovoEvento'
        self.titleInputID = 'com.claudivan.taskagenda:id/etTitulo'
        self.descriptionInputID = 'com.claudivan.taskagenda:id/etDescricao'
        self.taskCategory = "Task"
        self.rememberCategory = "Not Forget"
        self.upNavigationXpath = '//android.widget.ImageButton[@content-desc="Navigate up"]'
        self.categoryMenuID = 'com.claudivan.taskagenda:id/vgItemEtiqueta'
        self.confirmSaveID = 'com.claudivan.taskagenda:id/item_salvar'
        self.timePickerID = 'com.claudivan.taskagenda:id/btHora'
        self.datePickerID = 'com.claudivan.taskagenda:id/btData'
        self.categoryID = 'com.claudivan.taskagenda:id/vgItemEtiqueta'
        self.importantCategory = "Important"


    def goToAddEvent(self):
        self.driver.find_element_by_id(self.addButtonID).click()

    def inputTitle(self, title):
        self.driver.find_element_by_id(self.titleInputID).send_keys(title)

    def inputDescription(self, desc):
        self.driver.find_element_by_id(self.descriptionInputID).send_keys(desc)

    def pickDate(self, day, month, year):
        self.driver.find_element_by_id(self.datePickerID).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "android:id/datePicker")))
        self.driver.find_element_by_id("android:id/date_picker_header_year").click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//android.widget.TextView[@text='{year}']"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//android.widget.TextView[@text='{month}']"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//android.widget.TextView[@text='{day}']"))).click()
        self.driver.find_element_by_id("android:id/button1").click()


    def goBack(self):
        self.driver.find_element_by_xpath(self.upNavigationXpath).click()

    def confirmSaveEvent(self):
        self.driver.find_element_by_id(self.confirmSaveID).click()

    def chooseCategory(self, category):
        self.driver.find_element_by_id(self.categoryID).click()
        categoryToChoose = {
            'Important': self.importantCategory,
            'Task': self.taskCategory,
            'Not Forget': self.rememberCategory
        }.get(category)

        if categoryToChoose:
            self.driver.find_element_by_android_uiautomator(f'new UiSelector().text("{categoryToChoose}")').click()
        else:
            raise ValueError(f"Category {category} is not supported")

    def pickTime(self, hours, minutes):
        self.driver.find_element_by_id(self.timePickerID).click()
        self.driver.find_element_by_accessibility_id(" hours").send_keys(hours)
        self.driver.find_element_by_accessibility_id(" minutes").send_keys(minutes)
        self.driver.find_element_by_id("android:id/button1").click()


    def accessMenu(self):
        self.driver.find_element_by_id(self.categoryMenuID).click()
