from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    """Page Object для страницы «Лента заказов»"""

    def get_total_orders_count(self):
        return self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)

    def get_today_orders_count(self):
        return self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)

    def get_orders_in_progress(self):
        elements = self.wait.until(
            lambda d: d.find_elements(*OrderFeedLocators.ORDERS_IN_PROGRESS)
        )
        return [el.text for el in elements]