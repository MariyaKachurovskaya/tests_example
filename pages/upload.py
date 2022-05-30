import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Upload():
    """Страница загрузки файла"""

    FILE = (By.CSS_SELECTOR, '[type="file"]')
    UPLOAD_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    UPLOADED_FILES = (By.CSS_SELECTOR, '[id="uploaded-files"]')

    def __init__(self, browser):
        self.browser = browser
        self.url = "http://the-internet.herokuapp.com/upload"

    def open(self):
        """Открыть страницу"""

        self.browser.get(self.url)
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.FILE))
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.UPLOAD_BUTTON))

    def check_upload_file(self, file_path):
        """
        Проверить загрузку файла
        :param file_path: путь к загружаемому файлу
        """

        file = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.FILE))
        upload_button = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.UPLOAD_BUTTON))

        file.send_keys(*file_path)
        time.sleep(0.1)
        upload_button.click()

        upload_files = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.UPLOADED_FILES))
        assert file_path.split('\\')[-1] in upload_files.text
