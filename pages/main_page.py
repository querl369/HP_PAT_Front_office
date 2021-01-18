from .base_page import BasePage
from .locators import MainPage


class MainPage(BasePage):
    def go_to_login_page(self):
        # MainPageLocators will be unpacked as tuple e.g. (By.CSS_SELECTOR, '#login_link')
        login_link = self.browser.find_element(*MainPage.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPage.LOGIN_LINK), 'Login link is not presented'
