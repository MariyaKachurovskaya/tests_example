from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicControls():
    """Страница с динамическими контролов"""

    CHECKBOX = (By.CSS_SELECTOR, '[type="checkbox"]')
    ADD_REMOVE_BUTTON = (By.CSS_SELECTOR, '[type="button"][onclick="swapCheckbox()"]')

    def __init__(self, browser):
        self.browser = browser
        self.url = "http://the-internet.herokuapp.com/dynamic_controls"

    def open(self):
        """Открыть страницу"""

        self.browser.get(self.url)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.ADD_REMOVE_BUTTON))
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.CHECKBOX))

    def remove_checkbox(self):
        """Удалить чекбокс на странице"""

        button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.ADD_REMOVE_BUTTON))
        button.click()
        checkbox = self.browser.find_element(*self.CHECKBOX)
        state = WebDriverWait(self.browser, 5).until(
            EC.invisibility_of_element_located(checkbox))
        assert state is True

    def restore_checkbox(self):
        """Восстановить чекбокс"""

        button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.ADD_REMOVE_BUTTON))
        button.click()
        state = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.CHECKBOX))
        assert state is not False
