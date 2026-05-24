from selenium.webdriver.common.by import By

from page_objects.opencart.base_page import BasePage

class MainPage(BasePage):
    CHECK_H1 = (By.CSS_SELECTOR, "h1")
    CHECK_FEATURE = (By.CSS_SELECTOR, "#feature")
    CHECK_CLOUD = (By.CSS_SELECTOR, "#cloud")
    CHECK_BUSINESS = (By.CSS_SELECTOR, "#business")
    CHECK_MARKETPLACE = (By.CSS_SELECTOR, "#marketplace")

    def check_main_page(self):
        self.wait_element_visible(self.CHECK_H1)
        self.wait_element_visible(self.CHECK_FEATURE)
        self.wait_element_visible(self.CHECK_CLOUD)
        self.wait_element_visible(self.CHECK_BUSINESS)
        self.wait_element_visible(self.CHECK_MARKETPLACE)