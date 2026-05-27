from page_objects.prestashop.main_page import MainPage
from page_objects.prestashop.register_page import RegisterPage
from page_objects.prestashop.sign_in_page import SignInPage


def test_register_user(browser):
    MainPage(browser).sign_in()
    SignInPage(browser).move_to_register()
    RegisterPage(browser).register(
        user_firstname="Иван",
        user_lastname="Иванов",
        user_email="ivan.ivanov@gmail.com",
        user_password="ivan.ivanov1973",
        user_birthday="05/31/1973",
    )


def test_change_currency(browser):
    MainPage(browser).change_currency()