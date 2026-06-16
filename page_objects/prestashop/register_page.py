from selenium.webdriver.common.by import By
from .base_page import BasePage


class RegisterPage(BasePage):
    SOCIAL_TITLE_RADIO_MR = (By.XPATH, "//label[contains(., 'Mr.')]")
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "input[name='firstname']")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "input[name='lastname']")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    INPUT_BIRTHDAY = (By.CSS_SELECTOR, "input[name='birthday']")
    PRIVACY_POLICY_CHECKBOX = (By.XPATH, "(//*[contains(@class, 'custom-checkbox')])[2]")
    CUSTOMER_DATA_PRIVACY_CHECKBOX = (By.XPATH, "(//*[contains(@class, 'custom-checkbox')])[4]")
    SAVE_BTN = (By.CSS_SELECTOR, ".btn.btn-primary.form-control-submit.float-xs-right")

    def register(self, user_firstname: str, user_lastname: str, user_email: str, user_password: str, user_birthday: str):
        self.logger.info(f"{self.class_name}: Click Radio to select male social title")
        self.click(self.SOCIAL_TITLE_RADIO_MR)
        self.logger.info(f"{self.class_name}: Enter information in the firstname input")
        self.send_keys(self.INPUT_FIRSTNAME, user_firstname)
        self.logger.info(f"{self.class_name}: Enter information in the lastname input")
        self.send_keys(self.INPUT_LASTNAME, user_lastname)
        self.logger.info(f"{self.class_name}: Enter information in the email input")
        self.send_keys(self.INPUT_EMAIL, user_email)
        self.logger.info(f"{self.class_name}: Enter information in the password input")
        self.send_keys(self.INPUT_PASSWORD, user_password)
        self.logger.info(f"{self.class_name}: Enter information in the birthday input")
        self.send_keys(self.INPUT_BIRTHDAY, user_birthday)
        self.logger.info(f"{self.class_name}: Click Privacy Policy Checkbox")
        self.click(self.PRIVACY_POLICY_CHECKBOX)
        self.logger.info(f"{self.class_name}: Click Customer Data Privacy Checkbox")
        self.click(self.CUSTOMER_DATA_PRIVACY_CHECKBOX)
        self.logger.info(f"{self.class_name}: Click Save BTN")
        self.click(self.SAVE_BTN)
