from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    SIGN_IN_BTN = (By.CSS_SELECTOR, "#_desktop_user_info")
    CURRENT_CURRENCY = (By.CSS_SELECTOR, ".hidden-sm-down.btn-unstyle")
    NEW_CURRENCY = (By.CSS_SELECTOR, ".dropdown-menu.hidden-sm-down li:nth-child(2)")

    def sign_in(self):
        self.logger.info(f"{self.class_name}: Click Sign In BTN for Sign In: {self.SIGN_IN_BTN}")
        self.click(self.SIGN_IN_BTN)

    def change_currency(self):
        self.logger.info(f"{self.class_name}: Change Currency from {self.CURRENT_CURRENCY} to {self.NEW_CURRENCY}")
        self.click(self.CURRENT_CURRENCY)
        self.click(self.NEW_CURRENCY)
