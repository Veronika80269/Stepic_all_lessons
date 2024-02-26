from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/math.html")
    
#<input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    
#<button type="submit" class="btn btn-default" disabled>Submit</button>
    button_submit=browser.find_element(By.CLASS_NAME, "btn-default")
    button_disabled = button_submit.get_attribute("disabled")
    assert button_disabled =="true", " button_disabled is not selected by default"
 
    
finally:
    time.sleep(10)
    browser.quit()




