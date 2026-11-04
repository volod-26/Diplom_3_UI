from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from config import LOGIN_URL


class LoginPage(BasePage):
    """Page Object для страницы логина"""

    def open_login_page(self):
        self.open(LOGIN_URL)

    def login(self, email, password):
        self.fill(LoginPageLocators.EMAIL_INPUT, email)
        self.fill(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def click_login_link_on_register(self):
        self.click(MainPageLocators.LOGIN_LINK_ON_REGISTER)

    def click_restore_password_link(self):
        self.click(MainPageLocators.RESTORE_PASSWORD_LINK)