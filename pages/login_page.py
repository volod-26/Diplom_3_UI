from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators


class LoginPage:
    """Page Object для страницы логина"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, email, password):
        """Выполняет вход в систему"""
        self.wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()