from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def sum(x, y):
    return str(int(x) + int(y))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    time.sleep(2)
    

    num1= browser.find_element(By.ID, "num1")
    x=num1.text
    
    num2= browser.find_element(By.ID, "num2")
    y=num2.text
    
    sum1=sum(x, y)
 
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum1)
    

    button = browser.find_element( By.CLASS_NAME, "btn-default")
    button.click()
    
   
    
finally:
    time.sleep(10)
    browser.quit()




