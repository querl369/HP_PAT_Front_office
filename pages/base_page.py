from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LoginPage as LpL
from data import Urls
from data import Creds

class BasePage():
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def login_into_system(self, email, password):
        email_field = self.browser.find_element(*LpL.EMAIL_FIELD)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*LpL.PASSWORD_FIELD)
        pass_field.send_keys(password)
        login_btn = self.browser.find_element(*LpL.LOGIN_BTN)
        login_btn.click()
        WebDriverWait(self.browser, 5).until(
            EC.url_to_be(Urls.MAIN_PAGE)
        )
        assert 'import/request' in self.browser.current_url, "URL can't be reached"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

