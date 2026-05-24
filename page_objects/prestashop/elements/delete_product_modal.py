from selenium.webdriver.common.by import By
from .base_element import BaseElement


class DeleteProductModal(BaseElement):
    DELETE_SELECTION_BTN = (By.CSS_SELECTOR, ".btn.btn-primary.btn-lg.btn-confirm-submit")
    CLOSE_MODAL_BTN = (By.CSS_SELECTOR, ".btn.btn-primary.btn-lg.close-modal-button")

    def confirm_deleting(self):
        self.click(self.DELETE_SELECTION_BTN)
        self.click(self.CLOSE_MODAL_BTN)