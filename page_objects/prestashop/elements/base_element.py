
from ..base_page import BasePage


class BaseElement(BasePage):

    def open_iframe(self, locator: tuple):
        self.logger.debug("%s: Find and switch to iframe: %s" % (self.class_name, str(locator)))
        iframe = self.wait_element_visible(locator)
        self.driver.switch_to.frame(iframe)

    def close_iframe(self):
        self.logger.debug("%s: Switch to default page" % self.class_name)
        self.driver.switch_to.default_content()
