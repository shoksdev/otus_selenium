import allure

from config import PRESTASHOP_URL
from page_objects.prestashop.main_page import MainPage
from page_objects.prestashop.register_page import RegisterPage
from page_objects.prestashop.sign_in_page import SignInPage


@allure.suite("Регистрация нового пользователя в магазине prestashop")
def test_register_user(browser):
    with allure.step("Открываем главную страницу, после чего переходим к регистрации через страницу логина"):
        MainPage(browser).open(PRESTASHOP_URL)
        MainPage(browser).sign_in()
        SignInPage(browser).move_to_register()

    with allure.step("В форме регистрации вводим данные нового пользователя и регистрируем его"):
        RegisterPage(browser).register(
            user_firstname="Иван",
            user_lastname="Иванов",
            user_email="ivan.ivanov@gmail.com",
            user_password="ivan.ivanov1973",
            user_birthday="05/31/1973",
        )

@allure.suite("Переключение валют из верхнего меню prestashop")
def test_change_currency(browser):
    with allure.step("Открываем главную страницу и на ней меняем текущую валюту"):
        MainPage(browser).open(PRESTASHOP_URL)
        MainPage(browser).change_currency()