from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    time.sleep(2)
    

    treasure_picture = browser.find_element(By.ID, "treasure")
    x=treasure_picture.get_attribute("valuex")
    y = calc(x)

    input= browser.find_element(By.ID, "answer")
    input.send_keys(y)

    robot_checkbox= browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robots_radio= browser.find_element(By.ID, "robotsRule")
    robots_radio.click()

    button = browser.find_element( By.CLASS_NAME, "btn-default")
    button.click()



    
finally:
    time.sleep(10)
    browser.quit()



