import unittest
from selenium import webdriver
from pages.add_remove_elements import AddRemoveElements


class TestAddRemoveElements(unittest.TestCase):
    """Прверка добавления/удаления элементов"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome()
        cls.add_rem_page = AddRemoveElements(cls.browser)

    def setUp(self) -> None:
        self.add_rem_page.open()

    def test_01_add_and_remove_one_element(self):
        """Проверяем создание и удаление одного элемента.
        Объединила в один тест, т. к. они взаимозависимы"""

        self.add_rem_page.create_element()
        self.add_rem_page.delete_element()

    def test_02_add_and_remove_n_elements(self):
        """Проверяем создание и удаление нескольких элементов.
        Объединила в один тест, т. к. они взаимозависимы"""

        el_number = 3

        self.add_rem_page.create_elements(el_number)
        self.add_rem_page.delete_elements(el_number)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
