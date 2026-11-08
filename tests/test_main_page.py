import allure
from pages.main_page import MainPage
from config import BASE_URL


@allure.feature("Главная страница")
class TestMainPage:

    @allure.title("Переход на «Конструктор»")
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_order_feed_button()
        page.click_constructor_button()
        assert driver.current_url == f"{BASE_URL}/"

    @allure.title("Переход в «Ленту заказов»")
    def test_go_to_order_feed(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_order_feed_button()
        assert "feed" in driver.current_url

    @allure.title("Открытие модалки ингредиента")
    def test_open_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_bun_ingredient()
        assert page.is_ingredient_modal_visible()

    @allure.title("Закрытие модалки ингредиента")
    def test_close_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_bun_ingredient()
        page.close_ingredient_modal()
        assert not page.is_ingredient_modal_visible()

    @allure.title("Счётчик ингредиента существует")
    def test_bun_counter_exists(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        assert page.get_bun_counter() is not None