from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Целевые координаты (пиксели) – замените на свои
TARGET_X = 493
TARGET_Y = 260

def test_drag_stops_at_coordinates():
    # 1. Запускаем Chrome (GUI, каждый раз качает драйвер)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practice-automation.com/gestures/")

    # 2. Находим перетаскиваемый квадрат
    square = driver.find_element(By.ID, "moveMe")

    # 3. Перетаскиваем по 1 px, пока не достигнем нужных координат
    actions = ActionChains(driver)
    while True:
        # Читаем текущие координаты из CSS
        current_x = int(square.value_of_css_property("left").replace("px", ""))
        current_y = int(square.value_of_css_property("top").replace("px", ""))

        # Останавливаемся, когда близко (±1 px)
        if abs(current_x - TARGET_X) <= 1 and abs(current_y - TARGET_Y) <= 1:
            break

        # Микро-перетаскивание: 1 px вправо и 1 px вниз
        actions.drag_and_drop_by_offset(square, 1, 1).perform()
        time.sleep(0.05)   # небольшая пауза, чтобы не грузить CPU

    # 4. Проверяем, что квадрат именно на нужных координатах
    final_x = int(square.value_of_css_property("left").replace("px", ""))
    final_y = int(square.value_of_css_property("top").replace("px", ""))
    assert final_x == TARGET_X and final_y == TARGET_Y, \
        f"Квадрат не на {TARGET_X},{TARGET_Y}: получено {final_x},{final_y}"

    # 5. Закрываем браузер
    driver.quit()