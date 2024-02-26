from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")
   

    x_value = browser.find_element(By.ID, "input_value")
    x=x_value.text
    y=calc(x)
    
    browser.execute_script("window.scrollBy(0, 100);")

    answer= browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    option1 =browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 =browser.find_element(By.ID, 'robotsRule')
    option2.click()
   
    button= browser.find_element(By.TAG_NAME, "button")
    button.click


finally:
    time.sleep(30)
    browser.quit()




