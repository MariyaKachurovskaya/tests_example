import unittest
from selenium import webdriver
from pages.dynamic_controls import DynamicControls


class TestDynamicControls(unittest.TestCase):
    """Проверка страницы динамических контролов"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome()
        cls.dynamic_controls_page = DynamicControls(cls.browser)

    def setUp(self) -> None:
        self.dynamic_controls_page.open()

    def test_01_count_checkboxes(self):
        """Проверяем удаление и восстановление чекбокса"""

        self.dynamic_controls_page.remove_checkbox()
        self.dynamic_controls_page.restore_checkbox()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
