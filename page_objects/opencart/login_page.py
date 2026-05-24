from selenium.webdriver.common.by import By

from page_objects.opencart.base_page import BasePage

class LoginPage(BasePage):
    RESULT_LOGIN = (By.CSS_SELECTOR, ".col-md-9")

    def check_login(self):
        self.wait_element_visible(self.RESULT_LOGIN)
