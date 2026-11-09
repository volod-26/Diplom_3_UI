import allure
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
        assert response.status_code == 200, f"Ошибка: {response.text}"
        assert "order" in response.json(), f"Нет ключа order: {response.text}"

        page.wait_for_total_counter_increase(old_total)
        assert int(page.get_total_orders_count()) > old_total

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases(self, authorized_driver_with_token):
        driver, token = authorized_driver_with_token
        driver.get(FEED_URL)
        page = OrderFeedPage(driver)
        old_today = int(page.get_today_orders_count())

        ingredient_id = "691577430cc94f001a65b859"
        response = helpers.create_order_with_auth(token, [ingredient_id])
        assert response.status_code == 200, f"Ошибка: {response.text}"
        assert "order" in response.json(), f"Нет ключа order: {response.text}"

        page.wait_for_today_counter_increase(old_today)
        assert int(page.get_today_orders_count()) > old_today