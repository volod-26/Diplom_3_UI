from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    LOGIN_BUTTON_ON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    BUN_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    BUN_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter')]")