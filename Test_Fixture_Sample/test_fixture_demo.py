from selenium import webdriver
import pytest

driver = webdriver.Chrome(executable_path="./chromedriver.exe")


@pytest.fixture(autouse=True, scope="function")
def start_up():
    print("fixture start-up")
    pass


@pytest.fixture()
def teardown():
    print("Execution started")
    driver.get("https://www.google.com")
    driver.maximize_window()
    yield
    print("Execution completed")
    # driver.close()
    pass


@pytest.mark.demo
@pytest.mark.usefixtures("teardown")
def test1_launch_and_take_screenshot():
    driver.save_screenshot("Google_Search.png")
    print("test1 screenshot taken")
    print("title is:", driver.title)
    assert driver.title != "Google"


@pytest.mark.demo
@pytest.mark.usefixtures("teardown")
def test2_launch_and_take_screenshot():
    driver.save_screenshot("Google_Search_v1.png")
    print("test2 screenshot taken")
    print("title is:", driver.title)
    assert driver.title == "Google"
