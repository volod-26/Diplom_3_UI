import allure
import time
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from config import FEED_URL
import helpers


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_counter_increases(self, authorized_driver_with_token):
        driver, token = authorized_driver_with_token
        driver.get(FEED_URL)
        page = OrderFeedPage(driver)
        old_total = int(page.get_total_orders_count())

        ingredient_id = "691577430cc94f001a65b859"
        response = helpers.create_order_with_auth(token, [ingredient_id])
        assert response.status_code == 200, f"Ошибка при создании заказа: {response.text}"
        assert "order" in response.json(), f"В ответе нет ключа order: {response.text}"

        time.sleep(2)
        driver.refresh()
        new_total = int(page.get_total_orders_count())
        assert new_total > old_total

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases(self, authorized_driver_with_token):
        driver, token = authorized_driver_with_token
        driver.get(FEED_URL)
        page = OrderFeedPage(driver)
        old_today = int(page.get_today_orders_count())

        ingredient_id = "691577430cc94f001a65b859"
        response = helpers.create_order_with_auth(token, [ingredient_id])
        assert response.status_code == 200, f"Ошибка при создании заказа: {response.text}"
        assert "order" in response.json(), f"В ответе нет ключа order: {response.text}"

        # Ждём до 10 секунд, пока счётчик увеличится
        new_today = old_today
        for _ in range(10):
            time.sleep(1)
            driver.refresh()
            new_today = int(page.get_today_orders_count())
            if new_today > old_today:
                break

        assert new_today > old_today, f"Счётчик не увеличился: было {old_today}, стало {new_today}"

    @allure.title("Номер заказа появляется в разделе «В работе»")
    def test_order_number_in_progress(self, authorized_driver_with_token):
        driver, token = authorized_driver_with_token
        ingredient_id = "691577430cc94f001a65b859"
        response = helpers.create_order_with_auth(token, [ingredient_id])

        assert response.status_code == 200, f"Ошибка при создании заказа: {response.text}"
        assert "order" in response.json(), f"В ответе нет ключа order: {response.text}"

        order_number = str(response.json()["order"]["number"]).zfill(6)

        driver.get(FEED_URL)
        page = OrderFeedPage(driver)
        orders_in_progress = page.get_orders_in_progress()
        assert order_number in orders_in_progress