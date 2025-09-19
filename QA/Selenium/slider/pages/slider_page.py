from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver import ActionChains

class SliderPage(BasePage):
    URL = "https://practice-automation.com/slider/"

    SLIDER_INPUT = (By.CSS_SELECTOR, "input[type='range']")
    OUTPUT_VALUE = (By.ID, "value")

    def open(self):
        self.driver.get(self.URL)

    def get_current_value(self):
        return self.driver.find_element(*self.OUTPUT_VALUE).text

    def set_value_by_offset(self, percent: int):
        """Перемещаем слайдер на указанный процент (0-100)"""
        slider = self.driver.find_element(*self.SLIDER_INPUT)
        ActionChains(self.driver).drag_and_drop_by_offset(
            slider, percent * 2, 0  # 1 % ≈ 2 px (подстраивается под ширину)
        ).perform()

    def set_value_exact(self, target: int):
        """Точное значение через JS (быстро и надёжно)"""
        self.driver.execute_script(
            "arguments[0].value = arguments[1]; "
            "arguments[0].dispatchEvent(new Event('input'));",
            self.driver.find_element(*self.SLIDER_INPUT), target
        )