from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os
import softest


class test_asssertion_hard_soft(softest.TestCase):
    def test3_fetch_googlesearchbutton_text_and_assert_text(self):
        driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver.maximize_window()
        driver.get("https://www.google.com")
        button_text = driver.find_element_by_xpath(
            "//div[@class='FPdoLc lJ9FBc']//input[@value='Google Search']").get_attribute("value")
        ele = driver.find_element_by_xpath(
            "//div[@class='FPdoLc lJ9FBc']//input[@value='Google Search']")
        text = ele.text
        print("Text of the button is:", button_text)
        print("Using text property Text of the button is:", text)
        # this will fail so code will not go to next assert
        self.soft_assert(self.assertTrue, button_text == "Dinesh")
        # assert button_text == "Dinesh"
        # assert button_text == "Google Search"
        self.assert_all()
        driver.quit()

    pass

