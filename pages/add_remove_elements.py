import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddRemoveElements():
    """Страница для Добавления/удаления элементов"""

    ADD_ELEMENT = (By.CSS_SELECTOR, '.example > button')
    DELETE = (By.CSS_SELECTOR, '.example .added-manually')

    def __init__(self, browser):
        self.browser = browser
        self.url = "http://the-internet.herokuapp.com/add_remove_elements/"

    def open(self):
        """Открыть страницу"""

        self.browser.get(self.url)
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.ADD_ELEMENT))

    def create_element(self):
        """Добавить один элемент"""

        el_number_before = len(self.browser.find_elements(*self.DELETE))
        add_element = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.ADD_ELEMENT))
        add_element.click()
        time.sleep(1)
        el_number_after = len(self.browser.find_elements(*self.DELETE))
        assert el_number_after > el_number_before

    def create_elements(self, number):
        """
        Добавить несколько элементов
        :param number: число элементов, которые нужно добавить
        """

        for n in range(number):
            self.create_element()
            time.sleep(0.2)
        el_number_after = len(self.browser.find_elements(*self.DELETE))
        assert el_number_after == number

    def delete_element(self):
        """Удалить один элемент"""

        el_number_before = len(self.browser.find_elements(*self.DELETE))
        delete = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.DELETE))
        delete.click()
        time.sleep(1)
        el_number_after = len(self.browser.find_elements(*self.DELETE))
        assert el_number_after < el_number_before

    def delete_elements(self, number):
        """
        Удалить несколько элементов
        :param number: число элементов, которые нужно удалить"""

        el_number_before = len(self.browser.find_elements(*self.DELETE))
        for n in range(number):
            self.delete_element()
            time.sleep(0.2)
        el_number_after = len(self.browser.find_elements(*self.DELETE))
        assert el_number_after == el_number_before - number
