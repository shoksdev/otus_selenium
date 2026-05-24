from selenium.webdriver.common.by import By

from page_objects.opencart.base_page import BasePage

class CatalogPage(BasePage):
    CHECK_NAV = (By.CSS_SELECTOR, "nav")
    CHECK_PAGE_HEADER = (By.CSS_SELECTOR, ".page-header")
    CHECK_COL_1 = (By.CSS_SELECTOR, ".col-sm-4.col-md-3")
    CHECK_COL_2 = (By.CSS_SELECTOR, ".col-sm-8.col-md-9")
    CHECK_FILTER = (By.CSS_SELECTOR, "#collapse-filter")

    def check_catalog_page(self):
        self.wait_element_visible(self.CHECK_NAV)
        self.wait_element_visible(self.CHECK_PAGE_HEADER)
        self.wait_element_visible(self.CHECK_COL_1)
        self.wait_element_visible(self.CHECK_COL_2)
        self.wait_element_visible(self.CHECK_FILTER)