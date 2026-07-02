import pytest

from page_objects.opencart.catalog_page import CatalogPage


@pytest.mark.skip
def test_check_catalog(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.check_catalog_page()