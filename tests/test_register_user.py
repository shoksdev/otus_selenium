from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_register_user(browser, url):
    timeout = 120
    browser.get(f"{url}index.php?route=account/register")
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "h3")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-register")),
    )
