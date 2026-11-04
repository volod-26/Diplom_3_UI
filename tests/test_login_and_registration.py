import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config import REGISTER_URL, LOGIN_URL
import helpers


@allure.feature("Регистрация и Вход")
class TestLoginAndRegistration:

    @allure.title("Успешная регистрация")
    def test_successful_registration(self, driver):
        driver.get(REGISTER_URL)
        wait = WebDriverWait(driver, 10)

        email = f"{helpers.generate_random_string(10)}@yandex.ru"
        password = "password123"
        name = "Иван"

        # Ждём появления полей (на странице регистрации их 3)
        inputs = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input")))
        inputs[0].send_keys(name)   # Имя
        inputs[1].send_keys(email)  # Email
        inputs[2].send_keys(password)  # Пароль

        # Нажимаем «Зарегистрироваться»
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Зарегистрироваться']"))).click()

        # Ждём перехода на /login
        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    @allure.title("Ошибка при коротком пароле")
    def test_registration_with_short_password(self, driver):
        main_page = MainPage(driver)
        main_page.open(REGISTER_URL)
        main_page.register(helpers.generate_random_string(10) + "@yandex.ru", "123", "Иван")
        assert main_page.is_password_error_visible()

    @allure.title("Вход по кнопке «Войти в аккаунт» на главной")
    def test_login_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_login_button_on_main()
        assert "/login" in driver.current_url

    @allure.title("Вход через кнопку «Личный кабинет»")
    def test_login_from_personal_cabinet(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_personal_cabinet_button()
        assert "/login" in driver.current_url

    @allure.title("Вход через кнопку в форме регистрации")
    def test_login_from_registration_form(self, driver):
        login_page = LoginPage(driver)
        login_page.open(REGISTER_URL)
        login_page.click_login_link_on_register()
        assert "/login" in driver.current_url

    @allure.title("Вход через кнопку в форме восстановления пароля")
    def test_login_from_restore_password_form(self, driver):
        login_page = LoginPage(driver)
        login_page.open(LOGIN_URL)
        login_page.click_restore_password_link()
        assert "/forgot-password" in driver.current_url