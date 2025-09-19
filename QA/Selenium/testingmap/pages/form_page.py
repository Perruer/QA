from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class FormPage(BasePage):
    URL = "https://practice-automation.com/form-fields/"

    # ---------- поля ----------
    NAME_INPUT   = (By.ID, "name-input")
    EMAIL_INPUT  = (By.ID, "email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[type='password']")
    WATER_CHECKBOX = (By.CSS_SELECTOR, "[data-cy='drink1']")
    COLOR_RADIO  = (By.XPATH, "//input[@value='Red']")  # пример: красный цвет
    AUTOMATION_DROPDOWN = (By.CSS_SELECTOR, "select[data-cy='automation']")
    MESSAGE_AREA = (By.ID, "message")
    SUBMIT_BTN   = (By.XPATH, "//button[text()='Submit']")
    RESULT_TEXT  = (By.ID, "contact-form-success-header")

    def open(self):
        self.driver.get(self.URL)

    def fill_name(self, name):
        self.send_keys(self.NAME_INPUT, name)

    def fill_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    def fill_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    def check_water(self):
        self.click_js(self.WATER_CHECKBOX)

    def is_water_checked(self):
        return self.driver.find_element(*self.WATER_CHECKBOX).is_selected()

    def select_color_red(self):
        self.click(self.COLOR_RADIO)

    def select_automation_like(self, visible_text):
        
        dropdown = Select(self.wait.until(EC.presence_of_element_located(self.AUTOMATION_DROPDOWN)))
        dropdown.select_by_visible_text(visible_text)

    def fill_message(self, text):
        self.send_keys(self.MESSAGE_AREA, text)

    def submit_form(self):
        self.click_js(self.SUBMIT_BTN)

    def get_success_text(self):
        return self.get_text(self.RESULT_TEXT)