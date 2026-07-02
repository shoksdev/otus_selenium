import os
import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome",
                     choices=["chrome", "firefox"],
                     help="Browser: chrome or firefox")
    parser.addoption("--browser-version", default="125.0",
                     help="Browser version for Selenoid")
    parser.addoption("--executor", default="selenoid",
                     choices=["selenoid", "local"],
                     help="Where to run: selenoid or local")
    parser.addoption("--headless", action="store_true",
                     help="Run in headless mode")
    parser.addoption("--selenoid-url", default="http://selenoid:4444/wd/hub",
                     help="Selenoid URL")


def get_browser_options(browser_name, headless):
    """Создает опции для браузера"""

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        if headless:
            options.add_argument("--headless=new")
        return options

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        if headless:
            options.add_argument("--headless")
        return options

    raise ValueError(f"Unsupported browser: {browser_name}")


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Фикстура для создания WebDriver"""

    browser_name = request.param
    executor = request.config.getoption("--executor")
    browser_version = request.config.getoption("--browser-version")
    headless = request.config.getoption("--headless")
    selenoid_url = request.config.getoption("--selenoid-url")

    cli_browser = request.config.getoption("--browser")
    if cli_browser and cli_browser != browser_name:
        browser_name = cli_browser

    logger = logging.getLogger(request.node.name)
    os.makedirs("logs", exist_ok=True)

    file_handler = logging.FileHandler(f"logs/{request.node.name}.log", mode="w")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    options = get_browser_options(browser_name, headless)

    if executor == "local":
        logger.info(f"Starting local {browser_name}")
        if browser_name == "chrome":
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Firefox(options=options)

    else:
        logger.info(f"Starting {browser_name} on Selenoid")

        options.set_capability("browserName", browser_name)
        options.set_capability("browserVersion", browser_version)
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False,
            "sessionTimeout": "5m"
        })

        if browser_name == "firefox":
            options.set_capability("moz:firefoxOptions", {
                "args": ["--window-size=1920,1080", "--no-sandbox"],
                "prefs": {"browser.startup.homepage": "about:blank"}
            })

        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )

    driver.logger = logger
    driver.test_name = request.node.name

    yield driver

    driver.quit()