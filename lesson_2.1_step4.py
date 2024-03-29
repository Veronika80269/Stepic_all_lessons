from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CLASS_NAME, "form-control")
    answer.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
# успеваем скопировать код за 30 секунд
    time.sleep(30)
# закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла
