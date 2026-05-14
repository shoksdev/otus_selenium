from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_product_cart(browser, url):
    timeout = 5
    browser.get(f"{url}index.php?route=marketplace/extension/info&extension_id=38358")
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "h3")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#buy")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-md-8")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-md-4")),
    )
    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#comment-box")),
    )


def test_buy_product(browser, url):
    timeout = 5
    browser.get(f"{url}index.php?route=marketplace/extension/info&extension_id=38358")

    buy_btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg.btn-block")
    buy_btn.click()

    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "btn.btn-primary")),
    )

    buy_btn2 = browser.find_element(By.CSS_SELECTOR, "btn.btn-primary")
    buy_btn2.click()

