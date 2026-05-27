from page_objects.opencart.main_page import MainPage


def test_check_main(browser):
    main_page = MainPage(browser)
    main_page.check_main_page()
