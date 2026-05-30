from selenium.webdriver.common.by import By
from .base_element import BaseElement


class DeleteProductModal(BaseElement):
    DELETE_SELECTION_BTN = (By.CSS_SELECTOR, ".btn.btn-primary.btn-lg.btn-confirm-submit")
    CLOSE_MODAL_BTN = (By.CSS_SELECTOR, ".btn.btn-primary.btn-lg.close-modal-button")

    def confirm_deleting(self):
        self.logger.info(f"{self.class_name}: Click Delete Selection BTN")
        self.click(self.DELETE_SELECTION_BTN)
        self.logger.info(f"{self.class_name}: Click Close after deleting BTN")
        self.click(self.CLOSE_MODAL_BTN)