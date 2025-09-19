from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def test_google_title():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://google.com")
    assert "Google" in driver.title
    driver.quit()

def test_search_python():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://google.com")
    
    # Найти поле ввода (name="q") и ввести текст
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("python selenium tutorial")
    search_box.submit()          # нажать Enter
    
    # Проверить, что в title появилось слово python
    assert "python" in driver.title.lower()
    
    driver.quit()