from selenium.webdriver.common.by import By
from .base_page import BasePage


class AdminPage(BasePage):
    CATALOG_BTN = (By.CSS_SELECTOR, "#subtab-AdminCatalog")
    CATALOG_PRODUCTS_BTN = (By.XPATH, "//a[contains(text(), 'Products')]")

    def open_products(self):
        self.logger.info(f"{self.class_name}: Click Catalog BTN")
        self.click(self.CATALOG_BTN)
        self.logger.info(f"{self.class_name}: Click Catalog Products BTN")
        self.click(self.CATALOG_PRODUCTS_BTN)
