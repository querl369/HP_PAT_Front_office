from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    # TODO: write methods to fill test case
    def should_be_main_page(self):
        assert 'request' in self.browser.current_url, 'URL is incorrect'


