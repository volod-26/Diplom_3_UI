import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from config import LOGIN_URL


class LoginPage(BasePage):
    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self.open(LOGIN_URL)

    @allure.step("Войти в систему")
    def login(self, email, password):
        self.fill(LoginPageLocators.EMAIL_INPUT, email)
        self.fill(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Кликнуть на «Зарегистрироваться»")
    def click_register_link(self):
        self.click(LoginPageLocators.REGISTER_LINK)

    @allure.step("Кликнуть на «Восстановить пароль»")
    def click_restore_password_link(self):
        self.click(LoginPageLocators.RESTORE_PASSWORD_LINK)

    @allure.step("Кликнуть на «Войти» на странице регистрации")
    def click_login_link_on_register(self):
        self.click(LoginPageLocators.LOGIN_LINK_ON_REGISTER)