from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

def test_hover_fast(driver):
    driver.get("https://practice-automation.com/hover/")
    hover = driver.find_element(By.CSS_SELECTOR, "h3#mouse_over")
    ActionChains(driver).move_to_element(hover).perform()
    button = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3#mouse_over[style*='green']"))
    )
    assert button.is_displayed()