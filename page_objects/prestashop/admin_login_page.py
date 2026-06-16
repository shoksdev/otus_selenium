from selenium.webdriver.common.by import By
from .base_page import BasePage


class AdminLoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#passwd")
    LOGIN_BTN = (By.CSS_SELECTOR, "#submit_login")

    def admin_login(self, email, password):
        self.logger.info(f"{self.class_name}: Enter information in the Email input")
        self.send_keys(self.EMAIL_INPUT, email)
        self.logger.info(f"{self.class_name}: Enter information in the Password input")
        self.send_keys(self.PASSWORD_INPUT, password)
        self.logger.info(f"{self.class_name}: Click Login BTN")
        self.click(self.LOGIN_BTN)
