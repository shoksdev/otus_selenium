from selenium.webdriver.common.by import By
from .base_page import BasePage
from .elements.base_element import BaseElement


class CreateNewProductPage(BasePage):
    MENU_COLLAPSE = (By.CSS_SELECTOR, ".menu-collapse")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#product_header_name_1")
    PRICING_ELEMENT = (By.CSS_SELECTOR, "#product_pricing-tab-nav")
    RETAIL_PRICE_INPUT = (By.CSS_SELECTOR, 'input[name="product[pricing][retail_price][price_tax_excluded]"]')
    COST_PRICE_INPUT = (By.CSS_SELECTOR, 'input[name="product[pricing][wholesale_price]"]')

    SAVE_BTN = (By.CSS_SELECTOR, "#product_footer_save")


    def create_new_product(self, product_name, retail_price, cost_price):
        self.logger.info(f"{self.class_name}: Click Menu BTN to hide menu")
        self.click(self.MENU_COLLAPSE)

        self.logger.info(f"{self.class_name}: Enter information in the Product Name input")
        self.send_keys(self.PRODUCT_NAME_INPUT, product_name)

        self.logger.info(f"{self.class_name}: Click Pricing Tab")
        self.click(self.PRICING_ELEMENT)
        self.logger.info(f"{self.class_name}: Enter information in the Retail Price input")
        self.send_keys(self.RETAIL_PRICE_INPUT, retail_price)
        self.logger.info(f"{self.class_name}: Enter information in the Cost Price input")
        self.send_keys(self.COST_PRICE_INPUT, cost_price)

        self.logger.info(f"{self.class_name}: Find Save BTN")
        self.wait_element_visible(self.SAVE_BTN)
        self.logger.info(f"{self.class_name}: Click Save BTN")
        self.click(self.SAVE_BTN)
