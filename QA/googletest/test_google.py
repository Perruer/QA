from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_google_title():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://google.com")
    assert "Google" in driver.title
    driver.quit()