import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://localhost:8081/")


@pytest.fixture()
def browser(request):
    """Фикстура инициализации браузера"""

    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=options,)

        request.addfinalizer(driver.quit)

        driver.url = url

        def open(path=""):
            return driver.get(url + path)

        driver.maximize_window()
        driver.implicitly_wait(3)

        driver.open = open
        driver.open()

        return driver
