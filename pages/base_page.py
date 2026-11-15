import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент")
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти все элементы")
    def find_all(self, locator):
        return self.wait.until(lambda d: d.find_elements(*locator))

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Заполнить поле")
    def fill(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Обновить страницу")
    def refresh(self):
        self.driver.refresh()

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Перетащить элемент через JS-события")
    def drag_and_drop_js(self, source_locator, target_locator):
        source = self.wait.until(EC.presence_of_element_located(source_locator))
        target = self.wait.until(EC.presence_of_element_located(target_locator))
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var dataTransfer = new DataTransfer();
            var dragStartEvent = new DragEvent('dragstart', { dataTransfer: dataTransfer, bubbles: true });
            var dragOverEvent = new DragEvent('dragover', { dataTransfer: dataTransfer, bubbles: true });
            var dropEvent = new DragEvent('drop', { dataTransfer: dataTransfer, bubbles: true });
            source.dispatchEvent(dragStartEvent);
            target.dispatchEvent(dragOverEvent);
            target.dispatchEvent(dropEvent);
        """, source, target)

    @allure.step("Дождаться условия")
    def wait_until(self, condition):
        return self.wait.until(condition)