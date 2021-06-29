from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color:first-of-type")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group>a")
    PRODUCT_NAME_IN_ALERT = (
        By.CSS_SELECTOR,
        ".alert-noicon:first-of-type .alertinner strong"
    )
    PRODUCT_PRICE_IN_ALERT = (
        By.CSS_SELECTOR,
        ".alert-noicon:last-of-type .alertinner strong"
    )
    SUCCESS_MESSAGE = By.CSS_SELECTOR, ".alert-success"


class BasketPageLocators:
    TOTAL_PRICE = (By.CSS_SELECTOR, ".price_color:last-of-type")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".basket-items h3 a")
