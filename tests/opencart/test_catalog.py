from page_objects.opencart.catalog_page import CatalogPage


def test_check_catalog(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.check_catalog_page()