import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login():
    """Страница авторизации"""

    USERNAME = (By.NAME, 'username')
    PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button')
    LOGIN_ERROR = (By.CSS_SELECTOR, '.flash.error')

    def __init__(self, browser):
        self.browser = browser
        self.url = "http://the-internet.herokuapp.com/login"

    def open(self):

        self.browser.get(self.url)
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(self.USERNAME))
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(self.PASSWORD))
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(self.LOGIN_BUTTON))

    def login(self, login_str, password_str):
        """
        Авторизоваться на сайте
        :param login_str: Логин
        :param password_str: Пароль
        """

        login = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(self.USERNAME))
        password = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(self.PASSWORD))
        login_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(self.LOGIN_BUTTON))
        login.clear()
        password.clear()

        login.send_keys(*login_str)
        password.send_keys(*password_str)
        time.sleep(0.1)

        login_button.click()

    def check_login(self, login_str, password_str, result=True):
        """
        Проверить авторизацию
        :param login_str: Логин
        :param password_str: Пароль
        :param result: Ожидаемый результат авторизации - True, incorrect_password или incorrect_username
        """
        if result not in [True, 'incorrect_username', 'incorrect_password']:
            raise Exception('Результат может быть только True, incorrect_password или incorrect_username!')

        self.login(login_str, password_str)
        time.sleep(1)

        if result is True:
            login_result = WebDriverWait(self.browser, 5).until(
                EC.url_matches('http://the-internet.herokuapp.com/secure'))
            assert login_result is True
        elif result == 'incorrect_username':
            login_result = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(self.LOGIN_ERROR))
            assert 'Your username is invalid!' in login_result.text
        elif result == 'incorrect_password':
            login_result = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(self.LOGIN_ERROR))
            assert 'Your password is invalid!' in login_result.text
