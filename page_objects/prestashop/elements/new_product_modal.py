from selenium.webdriver.common.by import By
from .base_element import BaseElement


class NewProductModal(BaseElement):
    NEW_PRODUCT_IFRAME = (By.XPATH, '//*[@id="modal-create-product"]/div/div/div[2]/iframe')
    CLOSE_TOOLBAR_BTN = (By.XPATH, "//a[contains(@id, 'sfToolbarHideButton')]")
    STANDARD_PRODUCT_BTN = (By.XPATH, "//button[contains(., 'Standard product')]")
    ADD_NEW_PRODUCT_BTN = (By.XPATH, "//button[contains(., 'Add new product')]")

    def add_new_product(self):
        self.logger.info(f"{self.class_name}: Open Modal (iframe) to create new product")
        self.open_iframe(self.NEW_PRODUCT_IFRAME)

        self.logger.info(f"{self.class_name}: Close toolbar")
        self.click(self.CLOSE_TOOLBAR_BTN)
        self.logger.info(f"{self.class_name}: Create standard product")
        self.click(self.STANDARD_PRODUCT_BTN)
        self.logger.info(f"{self.class_name}: Create new product")
        self.click(self.ADD_NEW_PRODUCT_BTN)
        self.logger.info(f"{self.class_name}: Close modal (iframe)")

        self.close_iframe()

