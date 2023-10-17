from selenium import webdriver
import pytest


'''@pytest.mark.parametrize("search_text1",
                         [
                             "Dinesh",
                             "Pranav",
                             "Inderjit"
                         ]
                         )'''


@pytest.mark.parametrize("search_text",
                         [
                             "Dinesh",
                             "Pranav",
                             "Inderjit"
                         ]
                         )
# def test_check_parameter(search_text,search_text1):
def test_check_parameter(search_text):
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.google.com")
    driver.find_element_by_xpath("//*[@class='gLFyf']").send_keys(search_text)
    assert driver.title != "Google", "Actual vs Expected title is not matching"
    driver.quit()
    pass
