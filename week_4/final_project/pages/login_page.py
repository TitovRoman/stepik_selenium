from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, \
            'There is no substring "login" in URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'The login form was not found on the login page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'The register form was not found on the login page'

    def login_user(self, email, password):
        self.send_keys_to_element(
            LoginPageLocators.LOGIN_FORM_EMAIL,
            email
        )
        self.send_keys_to_element(
            LoginPageLocators.LOGIN_FORM_PASSWORD,
            password
        )
        self.click_to_element(LoginPageLocators.LOGIN_FORM_SUBMIT_BTN)

    def register_new_user(self, email, password):
        self.send_keys_to_element(
            LoginPageLocators.REGISTER_FORM_EMAIL,
            email
        )
        self.send_keys_to_element(
            LoginPageLocators.REGISTER_FORM_PASSWORD_1,
            password
        )
        self.send_keys_to_element(
            LoginPageLocators.REGISTER_FORM_PASSWORD_2,
            password
        )
        self.click_to_element(LoginPageLocators.REGISTER_FORM_SUBMIT_BTN)
