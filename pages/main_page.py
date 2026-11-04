from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from config import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    """Page Object для главной страницы"""

    def open_main_page(self):
        self.open(BASE_URL)

    def click_constructor_button(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed_button(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    def click_bun_ingredient(self):
        """Клик по ингредиенту (булке) через JS, чтобы обойти перекрытие картинкой"""
        element = self.wait.until(EC.presence_of_element_located(MainPageLocators.BUN_INGREDIENT))
        self.driver.execute_script("arguments[0].click();", element)

    def is_ingredient_modal_visible(self):
        try:
            return self.find(MainPageLocators.INGREDIENT_MODAL).is_displayed()
        except:
            return False

    def close_ingredient_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    def get_bun_counter(self):
        return self.get_text(MainPageLocators.BUN_COUNTER)

    # ===== НОВЫЕ МЕТОДЫ =====

    def register(self, email, password, name):
        # Находим все input'ы с name="name" (первый — Имя, второй — Email)
        inputs = self.driver.find_elements(By.XPATH, "//input[@name='name']")
        inputs[0].send_keys(name)   # Имя
        inputs[1].send_keys(email)  # Email
        self.fill(MainPageLocators.REGISTER_PASSWORD_INPUT, password)
        self.click(MainPageLocators.REGISTER_BUTTON)

    def click_login_button_on_main(self):
        self.click(MainPageLocators.LOGIN_BUTTON_ON_MAIN)

    def click_personal_cabinet_button(self):
        self.click(MainPageLocators.PERSONAL_CABINET_BUTTON)

    def click_login_link_on_register(self):
        self.click(MainPageLocators.LOGIN_LINK_ON_REGISTER)

    def click_restore_password_link(self):
        self.click(MainPageLocators.RESTORE_PASSWORD_LINK)

    def is_password_error_visible(self):
        try:
            return self.find(MainPageLocators.PASSWORD_ERROR).is_displayed()
        except:
            return False