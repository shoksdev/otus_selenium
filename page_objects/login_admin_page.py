from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage

class LoginAdminPage(BasePage):
    CHECK_H1 = (By.CSS_SELECTOR, "h1")
    CHECK_H2 = (By.CSS_SELECTOR, "h2")
    CHECK_DIV_P1 = (By.XPATH, "(//div[@class='col-sm-8']//p)[1]")
    CHECK_DIV_P2 = (By.XPATH, "(//div[@class='col-sm-8']//p)[2]")
    CHECK_ICON = (By.CSS_SELECTOR, ".icon")

    def check_login_admin_page(self):
        self.wait_element_visible(self.CHECK_H1)
        self.wait_element_visible(self.CHECK_H2)
        self.wait_element_visible(self.CHECK_DIV_P1)
        self.wait_element_visible(self.CHECK_DIV_P2)
        self.wait_element_visible(self.CHECK_ICON)