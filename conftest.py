import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
from config import BASE_URL, LOGIN_ENDPOINT
import helpers


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def authorized_driver_with_token(driver):
    user_data = helpers.register_new_user_and_return_login_password()
    if user_data:
        email, password, _ = user_data
        # Получаем токен
        login_response = requests.post(LOGIN_ENDPOINT, json={"email": email, "password": password})
        token = login_response.json()["accessToken"]
        yield driver, token
        # Удаляем пользователя после теста
        requests.delete(f"{BASE_URL}/auth/user", headers={"Authorization": token})
    else:
        yield driver, None