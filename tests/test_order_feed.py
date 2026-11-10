import allure
import time
from pages.order_feed_page import OrderFeedPage
import helpers


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_counter_increases(self, authorized_driver_with_token):
        driver, token = authorized_driver_with_token
        page = OrderFeedPage(driver)
        page.open_order_feed()
        old_total = int(page.get_total_orders_count())

        ingredient_id = "691577430cc94f001a65b859"
        response = helpers.create_order_with_auth(token, [ingredient_id])
        assert response.status_code == 200, f"Ошибка: {response.text}"
        assert "order" in response.json(), f"Нет ключа order: {response.text}"

        page.wait_for_total_counter_increase(old_total)
        assert int(page.get_total_orders_count()) > old_total

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases(self, authorized_driver_with_token):
        driver, token = authorized_driver_with_token
        page = OrderFeedPage(driver)
        page.open_order_feed()
        old_today = int(page.get_today_orders_count())

        ingredient_id = "691577430cc94f001a65b859"
        response = helpers.create_order_with_auth(token, [ingredient_id])
        assert response.status_code == 200, f"Ошибка: {response.text}"
        assert "order" in response.json(), f"Нет ключа order: {response.text}"

        page.wait_for_today_counter_increase(old_today)
        assert int(page.get_today_orders_count()) > old_today

    @allure.title("Номер заказа появляется в разделе «В работе»")
    def test_order_number_in_progress(self, authorized_driver_with_token):
        driver, token = authorized_driver_with_token
        ingredient_id = "691577430cc94f001a65b859"
        response = helpers.create_order_with_auth(token, [ingredient_id])

        assert response.status_code == 200, f"Ошибка: {response.text}"
        assert "order" in response.json(), f"Нет ключа order: {response.text}"

        order_number = str(response.json()["order"]["number"]).zfill(6)

        page = OrderFeedPage(driver)
        page.open_order_feed()

        orders_in_progress = []
        for _ in range(10):
            time.sleep(1)
            page.refresh()
            orders_in_progress = page.get_orders_in_progress()
            if order_number in orders_in_progress:
                break

        assert order_number in orders_in_progress, f"Заказ {order_number} не найден. В работе: {orders_in_progress}"