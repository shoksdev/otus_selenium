from page_objects.opencart.login_admin_page import LoginAdminPage


def test_check_login_admin(browser):
    login_admin_page = LoginAdminPage(browser)
    login_admin_page.check_login_admin_page()
