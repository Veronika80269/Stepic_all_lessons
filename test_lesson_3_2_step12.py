import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import unittest
import time

class TestInput(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1=browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input1.send_keys("Вероника")
 
        input2=browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input2.send_keys("Вероникjdyf")
    
        input3=browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input3.send_keys("вероника@mail.ru")
    
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        input4=browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input4.send_keys("Вероника")
 
        input5=browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input5.send_keys("Вероникjdyf")
    
        input6=browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input6.send_keys("вероника@mail.ru")
   
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        
        
        self.assertEqual(abs(input1, input2),"Should be absolute value of a number")
        self.assertEqual(abs(input3, input4),"Should be absolute value of a number")
        self.assertEqual(abs(input5, input6),"Should be absolute value of a number")


if __name__ == "__main__":
        pytest.main()
        








