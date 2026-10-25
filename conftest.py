import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import helpers
import requests


BASE_URL = "https://qa-stellarburgers.education-services.ru/api"


@pytest.fixture
def driver():
    """Фикстура для запуска и закрытия браузера Chrome"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://qa-stellarburgers.education-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def authorized_driver_with_token(driver):
    """Фикстура: создает пользователя, логинит через API, возвращает драйвер и токен"""
    user_data = helpers.register_new_user_and_return_login_password()
    if user_data:
        email, password, name = user_data
        login_response = requests.post(f"{BASE_URL}/auth/login", json={"email": email, "password": password})
        token = login_response.json()["accessToken"]

        # Логинимся в браузере через куки (чтобы не вводить пароль вручную)
        driver.get("https://qa-stellarburgers.education-services.ru/")
        driver.add_cookie({"name": "accessToken", "value": token.replace("Bearer ", ""), "domain": "qa-stellarburgers.education-services.ru"})
        driver.refresh()

        yield driver, token
        # Удаляем пользователя после теста
        requests.delete(f"{BASE_URL}/auth/user", headers={"Authorization": token})