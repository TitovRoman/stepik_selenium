from numbers import Number
from operator import attrgetter

from .base_page import BasePage
from .locators import BasketPageLocators
from ..utilities.price_utilities import get_float_price_from_str


class BasketPage(BasePage):
    def get_total_price(self) -> Number:
        price_str = self.browser.find_element(
            *BasketPageLocators.TOTAL_PRICE
        ).text
        return get_float_price_from_str(price_str)

    def get_products_name(self) -> list[str]:
        products_list = self.browser.find_elements(
            *BasketPageLocators.PRODUCT_NAME
        )
        return list(map(attrgetter('text'), products_list))

    def should_be_equal_product_names(self, product_names: list[str]) -> None:
        assert self.get_products_name() == product_names, \
            'The products in the basket does not match'

    def should_be_equal_price(self, price: Number) -> None:
        assert self.get_total_price() == price, \
            'The price in the basket does not match'
