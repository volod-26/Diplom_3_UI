from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


class MainPage:
    """Page Object для главной страницы Stellar Burgers"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _js_click(self, locator):
        """Клик через JavaScript (обход перекрытий)"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_constructor_button(self):
        """Клик по кнопке «Конструктор»"""
        self._js_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed_button(self):
        """Клик по кнопке «Лента заказов»"""
        self._js_click(MainPageLocators.ORDER_FEED_BUTTON)

    def click_bun_ingredient(self):
        """Клик по ингредиенту (булке)"""
        self._js_click(MainPageLocators.BUN_INGREDIENT)

    def is_ingredient_modal_visible(self):
        """Проверка, что всплывающее окно с деталями ингредиента открылось"""
        try:
            return self.wait.until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_MODAL)).is_displayed()
        except:
            return False

    def close_ingredient_modal(self):
        """Закрытие всплывающего окна по крестику"""
        self._js_click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_MODAL))

    def get_bun_counter(self):
        """Получение значения счётчика булки"""
        element = self.wait.until(EC.visibility_of_element_located(MainPageLocators.BUN_COUNTER))
        return element.text

    def click_order_button(self):
        """Клик по кнопке «Оформить заказ»"""
        self._js_click(MainPageLocators.ORDER_BUTTON)