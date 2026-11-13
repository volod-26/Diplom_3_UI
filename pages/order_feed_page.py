import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from config import FEED_URL


class OrderFeedPage(BasePage):
    @allure.step("Открыть ленту заказов")
    def open_order_feed(self):
        self.open(FEED_URL)

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_total_orders_count(self):
        return self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_today_orders_count(self):
        return self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)

    @allure.step("Получить список заказов в работе")
    def get_orders_in_progress(self):
        elements = self.find_all(OrderFeedLocators.ORDERS_IN_PROGRESS)
        return [el.text for el in elements]

    @allure.step("Дождаться появления заказа в разделе «В работе»")
    def wait_for_order_in_progress(self, order_number):
        def order_is_present(d):
            self.refresh()
            orders = self.get_orders_in_progress()
            return order_number in orders
        self.wait_until(order_is_present)

    @allure.step("Дождаться увеличения счётчика «за всё время»")
    def wait_for_total_counter_increase(self, old_count):
        for _ in range(10):
            self.refresh()
            new_count = int(self.get_total_orders_count())
            if new_count > old_count:
                return new_count
            self.wait_until(lambda d: False)

    @allure.step("Дождаться увеличения счётчика «за сегодня»")
    def wait_for_today_counter_increase(self, old_count):
        for _ in range(10):
            self.refresh()
            new_count = int(self.get_today_orders_count())
            if new_count > old_count:
                return new_count
            self.wait_until(lambda d: False)