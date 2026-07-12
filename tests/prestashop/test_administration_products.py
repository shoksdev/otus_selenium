import allure
import pytest

from config import PRESTASHOP_URL
from page_objects.prestashop.admin_login_page import AdminLoginPage
from page_objects.prestashop.admin_page import AdminPage
from page_objects.prestashop.admin_products_page import AdminProductsPage
from page_objects.prestashop.elements.delete_product_modal import DeleteProductModal
from page_objects.prestashop.elements.new_product_modal import NewProductModal
from page_objects.prestashop.create_new_product_page import CreateNewProductPage

ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "Admin123!"

@allure.suite("Добавление нового товара в разделе администратора")
def test_administration_create_product(browser):
    with allure.step(f"Входим в раздел администратора с учетными данными: {ADMIN_EMAIL}, {ADMIN_PASSWORD}"):
        AdminLoginPage(browser).open(f"{PRESTASHOP_URL}administration/index.php?controller=AdminLogin&token=1eef4e52612b001e19fed61be7b82010")
        AdminLoginPage(browser).admin_login(email=ADMIN_EMAIL, password=ADMIN_PASSWORD)

    with allure.step("Открываем раздел с товарами и инициируем добавление нового товара"):
        AdminPage(browser).open_products()
        AdminProductsPage(browser).new_product()
        NewProductModal(browser).add_new_product()

    with allure.step("Добавляем новый товар в форме"):
        CreateNewProductPage(browser).create_new_product(
            product_name="AeroPulse Smart Watch X2",
            retail_price="149.99",
            cost_price="82.50",
        )

@allure.suite("Удаление товара из списка в разделе администратора")
def test_administration_delete_product(browser):
    with allure.step(f"Входим в раздел администратора с учетными данными: {ADMIN_EMAIL}, {ADMIN_PASSWORD}"):
        AdminLoginPage(browser).open(f"{PRESTASHOP_URL}administration/index.php?controller=AdminLogin&token=1eef4e52612b001e19fed61be7b82010")
        AdminLoginPage(browser).admin_login(email=ADMIN_EMAIL, password=ADMIN_PASSWORD)

    with allure.step("Открываем раздел с товарами и выбираем последний добавленный товар в списке, после чего удаляем его"):
        AdminPage(browser).open_products()
        AdminProductsPage(browser).bulk_delete_product()
        DeleteProductModal(browser).confirm_deleting()
