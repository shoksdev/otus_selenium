from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = driver.logger
        self.class_name = type(self).__name__

    def open(self, url):
        self.logger.info("%s: Opening url: %s" % (self.class_name, url))
        self.driver.get(url)

    def click(self, locator: tuple, pause=0.1):
        self.logger.debug("%s: Clicking element: %s" % (self.class_name, str(locator)))
        ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))).pause(pause).click().perform()

    def clear(self, locator: tuple):
        self.logger.debug("%s: Clear input: %s" % (self.class_name, str(locator)))
        self.wait_element_visible(locator).clear()

    def send_keys(self, locator: tuple, keys: str):
        self.click(locator)
        self.clear(locator)
        self.logger.debug("%s: Send keys in input (%s): %s" % (self.class_name, str(locator), keys))
        self.wait_element_visible(locator).send_keys(keys)

    def wait_text_in_element(self, locator: tuple, text: str, timeout: int = 2):
        self.logger.debug("%s: Wait text in element (%s): %s" % (self.class_name, str(locator), text))
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def wait_element_visible(self, locator: tuple, timeout: int = 2):
        self.logger.debug("%s: Wait element is visible: %s" % (self.class_name, str(locator)))
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

