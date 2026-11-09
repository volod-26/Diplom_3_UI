import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from config import BASE_URL


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(BASE_URL)

    @allure.step("Кликнуть на «Конструктор»")
    def click_constructor_button(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на «Лента заказов»")
    def click_order_feed_button(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на «Войти в аккаунт»")
    def click_login_button_on_main(self):
        self.click(MainPageLocators.LOGIN_BUTTON_ON_MAIN)

    @allure.step("Кликнуть на «Личный кабинет»")
    def click_personal_cabinet_button(self):
        self.click(MainPageLocators.PERSONAL_CABINET_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_bun_ingredient(self):
        self.click(MainPageLocators.BUN_INGREDIENT)

    @allure.step("Проверить, что модалка ингредиента видима")
    def is_ingredient_modal_visible(self):
        try:
            return self.find(MainPageLocators.INGREDIENT_MODAL).is_displayed()
        except:
            return False

    @allure.step("Закрыть модалку ингредиента")
    def close_ingredient_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получить значение счётчика ингредиента")
    def get_bun_counter(self):
        return self.get_text(MainPageLocators.BUN_COUNTER)

    @allure.step("Перетащить булку в конструктор")
    def drag_and_drop_bun(self):
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCTOR_AREA)