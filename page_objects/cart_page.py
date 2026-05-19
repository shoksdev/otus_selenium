from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage

class CartPage(BasePage):
    CHECK_H3 = (By.CSS_SELECTOR, "h3")
    CHECK_BUY = (By.CSS_SELECTOR, "#buy")
    CHECK_COL1 = (By.CSS_SELECTOR, ".col-md-8")
    CHECK_COL2 = (By.CSS_SELECTOR, ".col-md-4")
    CHECK_COMMENT_BOX = (By.CSS_SELECTOR, "#comment-box")
    BUY_BTN = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg.btn-block")
    BUY_BTN_PRIMARY = (By.CSS_SELECTOR, "btn.btn-primary")

    def check_cart_page(self):
        self.wait_element_visible(self.CHECK_H3)
        self.wait_element_visible(self.CHECK_BUY)
        self.wait_element_visible(self.CHECK_COL1)
        self.wait_element_visible(self.CHECK_COL2)
        self.wait_element_visible(self.CHECK_COMMENT_BOX)

    def buy_product(self):
        self.click(self.BUY_BTN)
        self.wait_element_visible(self.BUY_BTN_PRIMARY)
        self.click(self.BUY_BTN_PRIMARY)
