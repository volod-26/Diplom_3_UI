from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы Stellar Burgers"""

    # Кнопка «Конструктор» в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

    # Кнопка «Лента заказов» в шапке
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")

    # Раздел «Булки» (ингредиент)
    BUN_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")

    # Всплывающее окно с деталями ингредиента
    INGREDIENT_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")

    # Крестик для закрытия всплывающего окна
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    # Счётчик ингредиента (булки)
    BUN_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter')]")

    # Кнопка «Оформить заказ» (появляется после добавления ингредиентов)
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")