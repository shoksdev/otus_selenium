import pytest
from page_objects.opencart.register_user_page import RegisterUserPage


@pytest.mark.skip
def test_check_register_user(browser):
    register_user_page = RegisterUserPage(browser)
    register_user_page.check_register_user_page()
