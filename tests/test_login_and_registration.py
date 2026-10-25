from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers
import time


class TestLoginAndRegistration:
    """Тесты для регистрации, входа, выхода и личного кабинета"""

    # ==================== РЕГИСТРАЦИЯ ====================

    def test_successful_registration(self, driver):
        """Успешная регистрация"""
        driver.get("https://qa-stellarburgers.education-services.ru/register")
        time.sleep(2)
        
        email = f"{helpers.generate_random_string(10)}@yandex.ru"
        password = helpers.generate_random_string(10)
        name = helpers.generate_random_string(10)
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input"))).send_keys(name)
        driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
        driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        
        wait.until(EC.url_contains("/login"))

    def test_registration_with_short_password(self, driver):
        """Ошибка при коротком пароле (меньше 6 символов)"""
        driver.get("https://qa-stellarburgers.education-services.ru/register")
        time.sleep(2)
        
        email = f"{helpers.generate_random_string(10)}@yandex.ru"
        password = "123"
        name = helpers.generate_random_string(10)
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input"))).send_keys(name)
        driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
        driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        
        error = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Некорректный пароль']")))
        assert error.text == "Некорректный пароль"

    # ==================== ВХОД ====================

    def test_login_from_main_page(self, driver):
        """Вход по кнопке «Войти в аккаунт» на главной"""
        driver.get("https://qa-stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))).click()
        wait.until(EC.url_contains("/login"))

    def test_login_from_personal_cabinet(self, driver):
        """Вход через кнопку «Личный кабинет»"""
        driver.get("https://qa-stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))).click()
        wait.until(EC.url_contains("/login"))

    def test_login_from_registration_form(self, driver):
        """Вход через кнопку в форме регистрации"""
        driver.get("https://qa-stellarburgers.education-services.ru/register")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))).click()
        wait.until(EC.url_contains("/login"))

    def test_login_from_restore_password_form(self, driver):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get("https://qa-stellarburgers.education-services.ru/login")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Восстановить пароль']"))).click()
        wait.until(EC.url_contains("/forgot-password"))

    # ==================== ЛИЧНЫЙ КАБИНЕТ ====================

    def test_go_to_personal_cabinet(self, driver):
        """Переход в личный кабинет"""
        user_data = helpers.register_new_user_and_return_login_password()
        email, password, name = user_data
        
        driver.get("https://qa-stellarburgers.education-services.ru/login")
        time.sleep(2)
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))).send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))).click()
        wait.until(EC.url_contains("/account"))

    def test_go_to_constructor_from_cabinet(self, driver):
        """Переход из личного кабинета в конструктор"""
        user_data = helpers.register_new_user_and_return_login_password()
        email, password, name = user_data
        
        driver.get("https://qa-stellarburgers.education-services.ru/login")
        time.sleep(2)
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))).send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Конструктор']"))).click()
        wait.until(EC.url_contains("/"))

    def test_logout(self, driver):
        """Выход из аккаунта"""
        user_data = helpers.register_new_user_and_return_login_password()
        email, password, name = user_data
        
        driver.get("https://qa-stellarburgers.education-services.ru/login")
        time.sleep(2)
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))).send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']"))).click()
        wait.until(EC.url_contains("/login"))