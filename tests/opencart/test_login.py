import pytest

from page_objects.opencart.login_page import LoginPage
from page_objects.opencart.elements.login_form import LoginForm


@pytest.mark.skip
def test_check_main(browser):
    login_page = LoginPage(browser)
    LoginForm(browser).login("test2@mail.ru", "Mypassword123!")
    login_page.check_login()
