from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_catalog(browser, url):
    timeout = 5
    browser.get(f"{url}index.php?route=marketplace/extension")
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "nav")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-header")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-sm-4.col-md-3")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-sm-8.col-md-9")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#collapse-filter")),
    )
