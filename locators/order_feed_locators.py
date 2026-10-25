from selenium.webdriver.common.by import By


class OrderFeedLocators:
    """Локаторы для страницы «Лента заказов»"""

    # Счётчик «Выполнено за всё время»
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")

    # Счётчик «Выполнено за сегодня»
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    # Раздел «В работе» (список заказов)
    ORDERS_IN_PROGRESS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul/li")