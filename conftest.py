import datetime
import os
import allure

import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServise
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when in ["setup", "call"] and rep.failed:

        browser = item.funcargs.get("browser")

        if browser:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            path = f"screenshots/{browser.test_name}_{timestamp}.png"

            browser.save_screenshot(path)

            with open(path, "rb") as file:
                allure.attach(
                    file.read(),
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            browser.logger.error(f"Screenshot saved: {path}")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    os.makedirs("logs", exist_ok=True)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log", mode="w")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test started at %s" % datetime.datetime.now())

    service = ChromeServise()
    options = Options()
    options.page_load_strategy = 'eager'
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=service, options=options)

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    def fin():
        driver.quit()
        logger.info("===> Test finished at %s" % datetime.datetime.now())

    request.addfinalizer(fin)
    return driver