from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os


def test1_launch_google_and_validate_title():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.maximize_window()
    driver.get("https://www.google.com")
    page_title = driver.title
    print("Page title is:", page_title)
    driver.quit()


def test2_launch_google_and_take_screenshot():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.maximize_window()
    driver.get("https://www.google.com")
    driver.save_screenshot("Window_Title.png")
    driver.quit()



