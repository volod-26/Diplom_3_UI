from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators.main_page_locators import MainPageLocators
import time
import helpers


class TestMainPage:
    """Тесты для главной страницы, конструктора и ленты заказов"""

    def _js_click(self, driver, locator):
        """Клик через JavaScript"""
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        driver.execute_script("arguments[0].click();", element)

    # ==================== КОНСТРУКТОР ====================

    def test_go_to_constructor(self, driver):
        """Переход по клику на «Конструктор»"""
        page = MainPage(driver)
        page.click_constructor_button()
        assert driver.current_url == "https://qa-stellarburgers.education-services.ru/"

    def test_go_to_buns_section(self, driver):
        """Переход к разделу «Булки»"""
        driver.get("https://qa-stellarburgers.education-services.ru/")
        self._js_click(driver, (By.XPATH, "//span[text()='Булки']"))
        assert "Булки" in driver.page_source

    def test_go_to_sauces_section(self, driver):
        """Переход к разделу «Соусы»"""
        driver.get("https://qa-stellarburgers.education-services.ru/")
        self._js_click(driver, (By.XPATH, "//span[text()='Соусы']"))
        assert "Соусы" in driver.page_source

    def test_go_to_fillings_section(self, driver):
        """Переход к разделу «Начинки»"""
        driver.get("https://qa-stellarburgers.education-services.ru/")
        self._js_click(driver, (By.XPATH, "//span[text()='Начинки']"))
        assert "Начинки" in driver.page_source

    def test_open_ingredient_modal(self, driver):
        """Если кликнуть на ингредиент, появляется всплывающее окно с деталями"""
        page = MainPage(driver)
        page.click_bun_ingredient()
        assert page.is_ingredient_modal_visible()

    def test_close_ingredient_modal(self, driver):
        """Всплывающее окно закрывается кликом по крестику"""
        page = MainPage(driver)
        page.click_bun_ingredient()
        assert page.is_ingredient_modal_visible()
        page.close_ingredient_modal()
        assert not page.is_ingredient_modal_visible()

    def test_bun_counter_exists(self, driver):
        """При добавлении ингредиента в заказ счётчик этого ингредиента существует"""
        page = MainPage(driver)
        page.click_bun_ingredient()
        page.close_ingredient_modal()
        time.sleep(2)
        assert page.get_bun_counter() is not None

    # ==================== ЛЕНТА ЗАКАЗОВ ====================

    def test_go_to_order_feed(self, driver):
        """Переход по клику на раздел «Лента заказов»"""
        page = MainPage(driver)
        page.click_order_feed_button()
        assert "feed" in driver.current_url

    def test_total_orders_counter_increases(self, authorized_driver_with_token):
        """При создании нового заказа счётчик «Выполнено за всё время» увеличивается"""
        driver, token = authorized_driver_with_token
        driver.get("https://qa-stellarburgers.education-services.ru/feed")
        time.sleep(2)
        page_feed = OrderFeedPage(driver)
        old_total = int(page_feed.get_total_orders_count())
        
        ingredient_id = "6acef97852135b001b21a32e"
        helpers.create_order_with_auth(token, [ingredient_id])
        
        driver.refresh()
        time.sleep(2)
        new_total = int(page_feed.get_total_orders_count())
        assert new_total > old_total

    def test_today_orders_counter_increases(self, authorized_driver_with_token):
        """При создании нового заказа счётчик «Выполнено за сегодня» увеличивается"""
        driver, token = authorized_driver_with_token
        driver.get("https://qa-stellarburgers.education-services.ru/feed")
        time.sleep(2)
        page_feed = OrderFeedPage(driver)
        old_today = int(page_feed.get_today_orders_count())
        
        ingredient_id = "6acef97852135b001b21a32e"
        helpers.create_order_with_auth(token, [ingredient_id])
        
        driver.refresh()
        time.sleep(2)
        new_today = int(page_feed.get_today_orders_count())
        assert new_today > old_today

    def test_order_number_in_progress(self, authorized_driver_with_token):
        """После оформления заказа его номер появляется в разделе «В работе»"""
        driver, token = authorized_driver_with_token
        ingredient_id = "6acef97852135b001b21a32e"
        response = helpers.create_order_with_auth(token, [ingredient_id])
        
        assert response.status_code == 200, f"Ошибка: {response.text}"
        order_number = str(response.json()["order"]["number"]).zfill(5)
        
        driver.get("https://qa-stellarburgers.education-services.ru/feed")
        page_feed = OrderFeedPage(driver)
        
        orders_in_progress = []
        for _ in range(10):
            time.sleep(1)
            orders_in_progress = page_feed.get_orders_in_progress()
            if order_number in orders_in_progress:
                break
        
        assert order_number in orders_in_progress, f"Заказ {order_number} не найден. В работе: {orders_in_progress}"