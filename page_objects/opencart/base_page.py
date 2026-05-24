from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator: tuple, pause=0.1):
        ActionChains(self.driver).move_to_element(
            WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(locator))
        ).pause(pause).click().perform()

    def wait_text_in_element(self, locator: tuple, text: str, timeout: int = 2):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def wait_element_visible(self, locator: tuple, timeout: int = 2):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))