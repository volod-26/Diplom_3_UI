import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import requests
from config import BASE_URL, LOGIN_ENDPOINT
import helpers


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    else:
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def authorized_driver_with_token(driver):
    user_data = helpers.register_new_user_and_return_login_password()
    if user_data:
        email, password, _ = user_data
        login_response = requests.post(LOGIN_ENDPOINT, json={"email": email, "password": password})
        token = login_response.json()["accessToken"]
        yield driver, token
        requests.delete(f"{BASE_URL}/api/auth/user", headers={"Authorization": token})
    else:
        yield driver, None