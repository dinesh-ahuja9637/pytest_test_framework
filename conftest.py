import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        #driver = webdriver.Chrome(executable_path="C:/Users/91976/PycharmProjects/PytestSampleProject/chromedriver.exe")
    '''elif request.param == "edge":
        print("ok")
        # driver = webdriver.Edge("./chromedriver.exe")'''
    request.cls.driver = driver
    driver.get("https://www.google.com/")
    print("browser:", request.param)
    print("opened browser")
    yield
    print("close driver")
    driver.close()
    pass
