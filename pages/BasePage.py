class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, ele):
        print("element located")
        return self.driver.find_element_by_xpath(ele)

    def enter_text(self, ele, txt):
        element = self.find_element(ele)
        element.send_keys(txt)
        print("text entered")
        pass

    pass
