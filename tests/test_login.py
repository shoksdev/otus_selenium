from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(browser, url):
    timeout = 30
    browser.get(f"{url}index.php?route=account/login")

    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")),
    )
    email_field = browser.find_element(By.CSS_SELECTOR, "#input-email")
    email_field.send_keys("pronyaavz@gmail.com")
    password_field = browser.find_element(By.CSS_SELECTOR, "#input-password")
    password_field.send_keys("ExeGnW!DX63xQVP")
    login_btn = browser.find_element(By.CSS_SELECTOR, ".btn btn-primary.btn-lg hidden-xs")
    login_btn.click()

    WebDriverWait(browser, timeout).until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-md-9")),
    )
