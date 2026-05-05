from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_login_admin(browser, url):
    timeout = 5
    browser.get(f"{url}administration")
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.XPATH, "(//div[@class='col-sm-8']//p)[1]")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.XPATH, "(//div[@class='col-sm-8']//p)[2]")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon")),
    )
