import pytest
from selenium import webdriver
import softest

pytestmark = pytest.mark.integeration

@pytest.mark.smoke
@pytest.mark.regression
def test4_click_button_and_verify_response():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.maximize_window()
    driver.get("http://demo.seleniumeasy.com/basic-radiobutton-demo.html")
    driver.find_element_by_xpath("//button[@id='buttoncheck']//preceding::input[@value='Male']").click()
    driver.find_element_by_xpath("//button[@id='buttoncheck']").click()
    txt = driver.find_element_by_xpath("//p[text()=\"Radio button 'Male' is checked\"]").text
    assert txt == '''Radio button 'Male' is checked'''
    driver.quit()
