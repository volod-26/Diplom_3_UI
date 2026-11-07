import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_total_orders_count(self):
        return self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_today_orders_count(self):
        return self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)

    @allure.step("Получить список заказов в работе")
    def get_orders_in_progress(self):
        elements = self.wait.until(
            lambda d: d.find_elements(*OrderFeedLocators.ORDERS_IN_PROGRESS)
        )
        return [el.text for el in elements]

    @allure.step("Дождаться увеличения счётчика «за сегодня»")
    def wait_for_today_counter_increase(self, old_count):
        for _ in range(10):
            self.refresh()
            new_count = int(self.get_today_orders_count())
            if new_count > old_count:
                return new_count
            self.wait.until(lambda d: False)
        return old_count