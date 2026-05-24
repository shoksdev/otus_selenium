from page_objects.prestashop.admin_login_page import AdminLoginPage
from page_objects.prestashop.admin_page import AdminPage
from page_objects.prestashop.admin_products_page import AdminProductsPage
from page_objects.prestashop.elements.delete_product_modal import DeleteProductModal
from page_objects.prestashop.elements.new_product_modal import NewProductModal
from page_objects.prestashop.create_new_product_page import CreateNewProductPage



def test_administration_create_product(browser):
    AdminLoginPage(browser).admin_login(email="admin@example.com", password="Admin123!")
    AdminPage(browser).open_products()
    AdminProductsPage(browser).new_product()
    NewProductModal(browser).add_new_product()
    CreateNewProductPage(browser).create_new_product(
        product_name="AeroPulse Smart Watch X2",
        retail_price="149.99",
        cost_price="82.50",
    )


def test_administration_delete_product(browser):
    AdminLoginPage(browser).admin_login(email="admin@example.com", password="Admin123!")
    AdminPage(browser).open_products()
    AdminProductsPage(browser).bulk_delete_product()
    DeleteProductModal(browser).confirm_deleting()

