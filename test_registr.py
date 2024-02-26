from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

answer = str(math.log(int(time.time())))

try:
    browser = webdriver.Chrome()
    browser.get(" https://stepik.org/lesson/236895/step/1")
    browser.implicitly_wait(5)
   
    button_login = browser.find_element(By.ID, "ember33")
    button_login.click()
    login = browser.find_element(By.ID, "id_login_email")
    login.send_keys(".........@mail.ru")
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("......")
    entrance = browser.find_element(By.CLASS_NAME, 'button_with-loader')
    entrance.click()
    
    
    password = browser.find_element(By.ID, "ember465")
    password.send_keys(answer)
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    

finally:

    time.sleep(30)
    browser.quit()
