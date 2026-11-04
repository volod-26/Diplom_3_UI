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

    # ===== НОВЫЕ ЛОКАТОРЫ ДЛЯ ТЕСТОВ =====

    # Кнопка «Войти в аккаунт» на главной
    LOGIN_BUTTON_ON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка «Личный кабинет» в шапке
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Сообщение об ошибке «Некорректный пароль»
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")

    # Поле «Имя» на форме регистрации (name="name")
    REGISTER_NAME_INPUT = (By.XPATH, "//input[@name='name']")

    # Поле «Email» на форме регистрации (name="name")
    REGISTER_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")

    # Поле «Пароль» на форме регистрации (name="Пароль")
    REGISTER_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")

    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Ссылка «Войти» на форме регистрации
    LOGIN_LINK_ON_REGISTER = (By.XPATH, "//a[text()='Войти']")

    # Ссылка «Восстановить пароль»
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")