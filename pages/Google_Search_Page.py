from pages import BasePage
from pages.BasePage import BasePage
from utilities.locators import Locators
from utilities.test_data import Test_Data


class GoogleSearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_search_text(self,ele,txt):
        self.enter_text(ele, txt)
        pass

    pass
