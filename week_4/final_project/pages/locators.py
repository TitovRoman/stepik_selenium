from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group>a")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_FORM_EMAIL = (By.ID, "id_login-username")
    LOGIN_FORM_PASSWORD = (By.ID, "id_login-password")
    LOGIN_FORM_SUBMIT_BTN = (By.NAME, "login_submit")

    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_FORM_EMAIL = (By.ID, "id_registration-email")
    REGISTER_FORM_PASSWORD_1 = (By.ID, "id_registration-password1")
    REGISTER_FORM_PASSWORD_2 = (By.ID, "id_registration-password2")
    REGISTER_FORM_SUBMIT_BTN = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color:first-of-type")
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
    MESSAGE_IN_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
