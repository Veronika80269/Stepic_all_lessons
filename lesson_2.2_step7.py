from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 


browser = webdriver.Chrome()
link="http://suninjuly.github.io/file_input.html"
browser.get(link)
   
input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
input1.send_keys( "Вероника")
    
input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
input2.send_keys( "Петрова")
    
input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
input3.send_keys( "Петровна")
    
current_dir = os.path.abspath(os.path.dirname(__file__))
prise_name = "prise.txt"
file_path = os.path.join(current_dir, prise_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

   
button= browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(30)
browser.quit()




