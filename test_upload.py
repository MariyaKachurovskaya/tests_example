import os
import unittest
from selenium import webdriver
from pages.upload import Upload


class TestUpload(unittest.TestCase):
    """Проверка загрузки файла"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome()
        cls.upload_page = Upload(cls.browser)

    def setUp(self) -> None:
        self.upload_page.open()

    def test_01_upload(self):
        """Проверяем загрузку файла на сайт"""

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'test_files\\example.txt')
        print(file_path)

        self.upload_page.check_upload_file(file_path)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
