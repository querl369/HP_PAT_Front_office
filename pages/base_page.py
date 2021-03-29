from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LoginPage as Lp, MainPage as Mp
from data import AssertionText as At, Urls, TelegramBot
import requests


class BasePage:
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def login_into_system(self, email, password):
        email_field = self.browser.find_element(*Lp.EMAIL_FIELD)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*Lp.PASSWORD_FIELD)
        pass_field.send_keys(password)
        login_btn = self.browser.find_element(*Lp.LOGIN_BTN)
        login_btn.click()
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(Mp.GENERATE_BTN)
        )
        assert 'import/request' in self.browser.current_url, "URL can't be reached"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Assert text for element is not presented
    @staticmethod
    def no_text(element):
        return At.TEXT_IN_ELEM + element + At.NOT_PRESENTED

    # Assert text for text in element is not presented
    @staticmethod
    def no_elem(element):
        return At.ELEM + element + At.NOT_PRESENTED

    def text_assert(self, how, what):
        return self.browser.find_element(how, what).text

    @staticmethod
    def send_test_case_to_telegram(case_name):
        payload_tuples = [TelegramBot.TESTCHATID, ('text', case_name + ' test case STARTED')]
        return requests.post(TelegramBot.HPATBOT, data=payload_tuples)
