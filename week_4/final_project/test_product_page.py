import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.need_review
@pytest.mark.parametrize('url', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
])
@pytest.mark.parametrize('query_string', [
    "?promo=offer0",
    "?promo=offer1",
    "?promo=offer2",
    "?promo=offer3",
    "?promo=offer4",
    "?promo=offer5",
    "?promo=offer6",
    pytest.param("?promo=offer7", marks=pytest.mark.xfail),
    "?promo=offer8",
    "?promo=offer9",
])
def test_guest_can_add_product_to_basket(browser, url, query_string):
    link = url + query_string
    page = ProductPage(browser, link, 3)
    page.open()
    price = page.get_price()
    product_name = page.get_product_name()
    page.add_product_to_basket_and_solve_quiz()
    page.check_price_in_alert()
    page.check_product_name_in_alert()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_equal_product_names([product_name])
    basket_page.should_be_equal_price(price)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link, 3)
    page.open()
    page.add_product_to_basket_and_solve_quiz()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link, 3)
    page.open()
    page.add_product_to_basket_and_solve_quiz()
    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue" \
           "/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue" \
           "/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue" \
           "/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url, 0)
    basket_page.should_be_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser

        register_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(self.browser, register_link)
        page.open()

        email = str(time.time()) + "@fakemail.org"
        password = '1Q%asW@!55sasw'

        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        link = "http://selenium1py.pythonanywhere.com/catalogue" \
               "/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(self.browser, link, 3)
        page.open()
        price = page.get_price()
        product_name = page.get_product_name()
        page.add_product_to_basket_and_solve_quiz()
        page.check_price_in_alert()
        page.check_product_name_in_alert()
        page.go_to_basket()
        basket_page = BasketPage(self.browser, self.browser.current_url)
        basket_page.should_be_equal_product_names([product_name])
        basket_page.should_be_equal_price(price)

    def test_user_cant_see_success_message(self):
        link = "http://selenium1py.pythonanywhere.com/catalogue" \
               "/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(self.browser, link, 3)
        page.open()
        page.should_not_be_success_message()
