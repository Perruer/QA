import pytest
from pages.form_page import FormPage

class TestFormFields:

    def test_open_form_page(self, driver):
        """1. Проверяем заголовок страницы формы"""
        page = FormPage(driver)
        page.open()
        assert "Form Fields" in driver.title, "Заголовок не содержит 'Form Fields'"

    def test_fill_and_submit_form(self, driver):
        """2. Заполняем все поля и жмём Submit -> проверяем сообщение об успехе"""
        page = FormPage(driver)
        page.open()

        page.fill_name("Иван")
        page.fill_email("ivan@test.ru")
        page.fill_password("Qwerty123")
        page.check_water()
        page.select_color_red()
        page.fill_message("Привет из автотеста!")
        page.select_automation_like("Yes")
        page.submit_form()

        # success = page.get_success_text()
        # assert "Message received!" in success, \
        #        f"Сообщение об успехе не появилось: {success}"



        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        print("Alert text:", alert.text)
        assert alert.text == "Message received!", f"Неожиданный текст: {alert.text}"
        alert.accept()