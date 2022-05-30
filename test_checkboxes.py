import unittest
from selenium import webdriver
from pages.checkboxes import Checkboxes


class TestCheckboxes(unittest.TestCase):
    """Проверка чекбоксов"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome()
        cls.checkboxes_page = Checkboxes(cls.browser)

    def setUp(self) -> None:
        self.checkboxes_page.open()

    def test_01_count_checkboxes(self):
        """Проверяем количество чекбоксов на странице"""

        self.checkboxes_page.check_number_of_checkboxes(2)

    def test_02_select_checkbox(self):
        """Проверяем возможность выбора верхнего и нижнего чекбоксов"""
        self.checkboxes_page.select_checkbox(1, True)
        self.checkboxes_page.select_checkbox(1, False)
        self.checkboxes_page.select_checkbox(2, False)
        self.checkboxes_page.select_checkbox(2, True)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
