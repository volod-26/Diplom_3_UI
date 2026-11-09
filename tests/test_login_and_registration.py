import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from config import REGISTER_URL, LOGIN_URL


@allure.feature("Регистрация и Вход")
class TestLoginAndRegistration:

    @allure.title("Успешная регистрация")
    def test_successful_registration(self, driver):
        page = LoginPage(driver)
        page.open(REGISTER_URL)
        assert "/register" in page.get_current_url()

    @allure.title("Вход по кнопке на главной")
    def test_login_from_main_page(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_login_button_on_main()
        assert "/login" in page.get_current_url()

    @allure.title("Вход через «Личный кабинет»")
    def test_login_from_personal_cabinet(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_personal_cabinet_button()
        assert "/login" in page.get_current_url()

    @allure.title("Вход через кнопку в форме регистрации")
    def test_login_from_registration_form(self, driver):
        page = LoginPage(driver)
        page.open(REGISTER_URL)
        page.click_login_link_on_register()
        assert "/login" in page.get_current_url()

    @allure.title("Вход через кнопку в форме восстановления пароля")
    def test_login_from_restore_password_form(self, driver):
        page = LoginPage(driver)
        page.open(LOGIN_URL)
        page.click_restore_password_link()
        assert "/forgot-password" in page.get_current_url()