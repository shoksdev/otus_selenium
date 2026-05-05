from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_main(browser, url):
    timeout = 3
    browser.get(url)
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#feature")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#cloud")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#business")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#marketplace")),
    )
