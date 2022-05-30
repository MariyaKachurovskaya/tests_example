import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkboxes():
    """Страница с двумя чекбоксами"""

    CHECKBOX = (By.XPATH, '//*[@id="checkboxes"]/input')

    def __init__(self, browser):
        self.browser = browser
        self.url = "http://the-internet.herokuapp.com/checkboxes"

    def open(self):
        """Открыть страницу"""

        self.browser.get(self.url)
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.CHECKBOX))

    def check_number_of_checkboxes(self, number):
        """
        Проверить количество чекбоксов на странице
        :param number: ожидаемое количество чекбоксов
        """

        assert number == len(self.browser.find_elements(*self.CHECKBOX))

    def select_checkbox(self, number, state):
        """
        Выделить чекбокс
        :param number: порядковый номер чекбокса, который выбираем
        :param state: ожидаемое состояние чекбокса после выбора
        """

        checkbox = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((self.CHECKBOX[0], self.CHECKBOX[1] + f'[{number}]')))
        checkbox.click()
        time.sleep(0.1)
        assert checkbox.is_selected() == state
