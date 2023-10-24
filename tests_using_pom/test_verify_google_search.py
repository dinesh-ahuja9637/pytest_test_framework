from pages import BasePage
from tests_using_pom.test_basetest import BaseTest
from pages.Google_Search_Page import GoogleSearchPage
from utilities.locators import Locators
from utilities.test_data import Test_Data


class TestGoogle(BaseTest):

    def test_launch_google(self):
        google_search_page = GoogleSearchPage(self.driver)
        google_search_page.enter_text(Locators.google_search_box,Test_Data.text)

        pass
    pass
