from page_objects.cart_page import CartPage


def test_check_product_cart(browser):
    cart_page = CartPage(browser)
    cart_page.check_cart_page()


def test_buy_product(browser):
    cart_page = CartPage(browser)
    cart_page.buy_product()


