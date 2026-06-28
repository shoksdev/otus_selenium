import datetime
import os
import allure
import pytest
import logging
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", default="selenoid")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")

    logger = logging.getLogger(request.node.name)
    os.makedirs("logs", exist_ok=True)

    file_handler = logging.FileHandler(
        f"logs/{request.node.name}.log",
        mode="w"
    )
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))

    logger.addHandler(file_handler)
    logger.setLevel(log_level)

    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    options.set_capability("browserName", browser_name)
    options.set_capability("browserVersion", "127.0")
    options.set_capability(
        "selenoid:options",
        {
            "enableVNC": True,
            "enableVideo": False,
            "sessionTimeout": "1m"
        }
    )

    if executor == "selenoid":
        driver = webdriver.Remote(
            command_executor="http://selenoid:4444/wd/hub",
            options=options
        )
    else:
        driver = webdriver.Chrome(options=options)

    driver.logger = logger
    driver.test_name = request.node.name

    yield driver

    driver.quit()
