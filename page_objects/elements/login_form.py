from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginForm(BasePage):
    FROM_BUTTON = (By.CSS_SELECTOR, ".btn btn-primary.btn-lg hidden-xs")

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
        self.click(FROM_BUTTON)
