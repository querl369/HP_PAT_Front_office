from selenium.common.exceptions import NoSuchElementException
from pages.locators import LoginPageLocators as LpL
from data import Creds

class BasePage():
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def login_into_system(self, email, password):
        email_field = self.browser.find_element(*LpL.EMAIL_FIELD)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*LpL.PASSWORD_FIELD)
        pass_field.send_keys(password)
        login_btn = self.browser.find_element(*LpL.LOGIN_BTN)
        login_btn.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

