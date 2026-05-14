import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://www.opencart.com/")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        service = Service()
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Driver not supported")

    request.addfinalizer(driver.quit)

    return driver

@pytest.fixture
def url(request):
    return request.config.getoption("--url")
