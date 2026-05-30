from selenium.webdriver.common.by import By
from .base_page import BasePage


class AdminProductsPage(BasePage):
    NEW_PRODUCT_BTN = (By.CSS_SELECTOR, "#page-header-desc-configuration-add")
    LAST_PRODUCT_CHECKBOX = (By.XPATH, "(//*[contains(@class, 'bulk_action-type column-bulk')])[1]")
    BULK_ACTIONS_BUTTON = (By.CSS_SELECTOR, ".btn.btn-outline-secondary.dropdown-toggle.js-bulk-actions-btn")
    DELETE_SELECTION_BUTTON = (By.CSS_SELECTOR, "#product_grid_bulk_action_bulk_delete_ajax")

    def new_product(self):
        self.logger.info(f"{self.class_name}: Click New Product BTN")
        self.click(self.NEW_PRODUCT_BTN)

    def bulk_delete_product(self):
        self.click(self.LAST_PRODUCT_CHECKBOX)
        self.logger.info(f"{self.class_name}: Click Last Created Product Checkbox")
        self.click(self.BULK_ACTIONS_BUTTON)
        self.logger.info(f"{self.class_name}: Click Bulk Actions Btn")
        self.click(self.DELETE_SELECTION_BUTTON)
        self.logger.info(f"{self.class_name}: Click Delete Selection Btn")