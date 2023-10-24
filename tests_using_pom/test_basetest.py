from pages import BasePage
import pytest
import utilities.locators


@pytest.mark.usefixtures("initialize_driver")
class BaseTest:
    def demo_func(self):
        pass
    pass
