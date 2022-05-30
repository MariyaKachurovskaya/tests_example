import unittest
from selenium import webdriver
from pages.login import Login


class TestLogin(unittest.TestCase):
    """Проверяем авторизацию на сайте"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome()
        cls.login_page = Login(cls.browser)

    def setUp(self) -> None:
        self.login_page.open()

    def test_01_correct_data(self):
        """Проверяем авторизацию с корректными данными"""

        self.login_page.check_login('tomsmith', 'SuperSecretPassword!', True)

    def test_02_incorrect_login(self):
        """Проверяем авторизацию с некорректным логином"""

        self.login_page.check_login('tomsmith123', 'SuperSecretPassword!', 'incorrect_username')

    def test_03_incorrect_password(self):
        """Проверяем авторизацию с некорректным паролем"""

        self.login_page.check_login('tomsmith', '654656', 'incorrect_password')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
