from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import helpers


class TestOrderFeed:
    """Тесты для раздела «Лента заказов»"""

    def test_total_orders_counter_increases(self, authorized_driver_with_token):
        """При создании нового заказа счётчик «Выполнено за всё время» увеличивается"""
        driver, token = authorized_driver_with_token
        
        driver.get("https://qa-stellarburgers.education-services.ru/feed")
        time.sleep(2)
        page_feed = OrderFeedPage(driver)
        old_total = int(page_feed.get_total_orders_count())
        
        ingredient_id = "6acef97852135b001b21a32e"
        response = helpers.create_order_with_auth(token, [ingredient_id])
        
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
        response = helpers.create_order_with_auth(token, [ingredient_id])
        
        driver.refresh()
        time.sleep(2)
        new_today = int(page_feed.get_today_orders_count())
        
        assert new_today > old_today

    def test_order_number_in_progress(self, authorized_driver_with_token):
        """После оформления заказа его номер появляется в разделе «В работе»"""
        driver, token = authorized_driver_with_token
        
        ingredient_id = "6acef97852135b001b21a32e"
        response = helpers.create_order_with_auth(token, [ingredient_id])
        
        assert response.status_code == 200, f"Ошибка при создании заказа: {response.text}"
        
        # Приводим номер к формату с ведущими нулями (как в ленте)
        order_number = str(response.json()["order"]["number"]).zfill(5)
        
        driver.get("https://qa-stellarburgers.education-services.ru/feed")
        
        # Ждем, пока заказ появится в ленте (до 10 секунд)
        page_feed = OrderFeedPage(driver)
        orders_in_progress = []
        for _ in range(10):
            time.sleep(1)
            orders_in_progress = page_feed.get_orders_in_progress()
            if order_number in orders_in_progress:
                break
        
        assert order_number in orders_in_progress, f"Заказ {order_number} не появился в ленте. Текущие заказы: {orders_in_progress}"