from selenium import webdriver
import pytest


@pytest.mark.usefixtures("initialize_driver")
class BaseClass:
    pass


#@pytest.mark.skip(reason="skipping the class")
@pytest.mark.usefixtures("initialize_driver")
class Test_ChildClass:
    def test1_launch_google(self):
        self.driver.get("http://www.google.com")
        self.driver.maximize_window()
        text = self.driver.title
        assert text == "Google"

    @pytest.mark.skip(reason="not needed")
    def test2_launch_google(self):
        #pytest.skip("Skiping this test")
        self.driver.get("http://www.google.com")
        self.driver.maximize_window()
        text = self.driver.title
        assert text == "Google"

    @pytest.mark.xfail(reason="Should fail")
    def test3_launch_google(self):
        self.driver.get("http://www.google.com")
        self.driver.maximize_window()
        text = self.driver.title
        assert text != "Google"
