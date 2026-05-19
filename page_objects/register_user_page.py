from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage

class RegisterUserPage(BasePage):
    CHECK_H3 = (By.CSS_SELECTOR, "h3")
    CHECK_INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    CHECK_INPUT_EMAIL = (By.XPATH, "#input-email")
    CHECK_INPUT_PASSWORD = (By.XPATH, "#input-password")
    CHECK_BUTTON_REGISTER = (By.CSS_SELECTOR, "#button-register")

    def check_register_user_page(self):
        self.wait_element_visible(self.CHECK_H3)
        self.wait_element_visible(self.CHECK_INPUT_USERNAME)
        self.wait_element_visible(self.CHECK_INPUT_EMAIL)
        self.wait_element_visible(self.CHECK_INPUT_PASSWORD)
        self.wait_element_visible(self.CHECK_BUTTON_REGISTER)