from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage:
    """Page Object для страницы «Лента заказов»"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_total_orders_count(self):
        """Получение значения счётчика «Выполнено за всё время»"""
        return self.wait.until(EC.visibility_of_element_located(OrderFeedLocators.TOTAL_ORDERS_COUNTER)).text

    def get_today_orders_count(self):
        """Получение значения счётчика «Выполнено за сегодня»"""
        return self.wait.until(EC.visibility_of_element_located(OrderFeedLocators.TODAY_ORDERS_COUNTER)).text

    def get_orders_in_progress(self):
        """Получение списка номеров заказов в разделе «В работе»"""
        elements = self.wait.until(EC.presence_of_all_elements_located(OrderFeedLocators.ORDERS_IN_PROGRESS))
        return [element.text for element in elements]