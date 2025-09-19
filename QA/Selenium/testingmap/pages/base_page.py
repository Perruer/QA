from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 1)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def is_selected(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).is_selected()
    
    def click_js(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)