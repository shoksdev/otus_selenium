import pytest

from page_objects.opencart.cart_page import CartPage

@pytest.mark.skip
def test_check_product_cart(browser):
    cart_page = CartPage(browser)
    cart_page.check_cart_page()

@pytest.mark.skip
def test_buy_product(browser):
    cart_page = CartPage(browser)
    cart_page.buy_product()


