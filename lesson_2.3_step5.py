from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
   
    button = browser.find_element(By.TAG_NAME, "button")
    button.click() 
    
    browser.switch_to.window(browser.window_handles[1])
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    decision=calc(x)
    
    answer=browser.find_element(By.CLASS_NAME, "form-control")
    answer.send_keys(decision)
    
    button= browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    
    
   
   
  
finally:
    time.sleep(30)
    browser.quit()



