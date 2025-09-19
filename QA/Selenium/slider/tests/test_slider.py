import pytest
from pages.slider_page import SliderPage

class TestSlider:

    def test_slider_js_exact(self, driver):
        """Устанавливаем значение 75 через JS и проверяем отображение"""
        page = SliderPage(driver)
        page.open()

        page.set_value_exact(75)
        actual = page.get_current_value()

        assert actual == "75", f"Ожидалось 75, получено {actual}"

    def test_slider_offset(self, driver):
        """Перемещаем мышью на ~50 % и проверяем, что значение изменилось"""
        page = SliderPage(driver)
        page.open()

        start = page.get_current_value()
        page.set_value_by_offset(50)
        finish = page.get_current_value()

        assert start != finish, "Значение не изменилось после drag-and-drop"