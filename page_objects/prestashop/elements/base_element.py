
from ..base_page import BasePage


class BaseElement(BasePage):

    def open_iframe(self, locator: tuple):
        iframe = self.wait_element_visible(locator)
        self.driver.switch_to.frame(iframe)

    def close_iframe(self):
        self.driver.switch_to.default_content()
