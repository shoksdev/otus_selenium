from selenium.webdriver.common.by import By
from .base_page import BasePage


class SignInPage(BasePage):
    REGISTER_BTN = (By.XPATH, '//*[contains(text(), "No account? Create one here")]')

    def move_to_register(self):
        self.logger.info(f"{self.class_name}: Click Register BTN in: {self.REGISTER_BTN}")
        self.click(self.REGISTER_BTN)