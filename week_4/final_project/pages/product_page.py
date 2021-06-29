from .base_page import BasePage
from .locators import ProductPageLocators
from ..utilities.price_utilities import get_float_price_from_str


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        button.click()

    def add_product_to_basket_and_solve_quiz(self):
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()

    def _get_price(self, locator) -> float:
        price_str = self.browser.find_element(
            *locator
        ).text
        return get_float_price_from_str(price_str)

    def _get_product_name(self, locator) -> str:
        return self.browser.find_element(
            *locator
        ).text

    def get_price(self) -> float:
        return self._get_price(ProductPageLocators.PRODUCT_PRICE)

    def get_product_name(self) -> str:
        return self._get_product_name(ProductPageLocators.PRODUCT_NAME)

    def get_price_from_alert(self) -> float:
        return self._get_price(ProductPageLocators.PRODUCT_PRICE_IN_ALERT)

    def get_product_name_from_alert(self) -> str:
        return self._get_product_name(ProductPageLocators.PRODUCT_NAME_IN_ALERT)

    def check_product_name_in_alert(self):
        assert self.get_product_name() == self.get_product_name_from_alert(), \
            'Name in alert does not match with product name'

    def check_price_in_alert(self):
        assert self.get_price() == self.get_price_from_alert(), \
            'Price in alert does not match with product price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def go_to_basket(self):
        basket_button = self.browser.find_element(
            *ProductPageLocators.BASKET_BUTTON
        )
        basket_button.click()
