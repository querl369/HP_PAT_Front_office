from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPage as Mp
from data import TextMainPage as Tm, AssertionText as At, Urls
import time



class MainPage(BasePage):
    # MAIN elements on the page


    def should_be_main_page(self):
        assert Urls.MAIN_PAGE in self.browser.current_url, 'URL is incorrect'

    # MENU dropdown methods block started
    def should_be_menu_dropdown(self):
        assert self.is_element_present(*Mp.MENU_DROPDOWN_MAIN), At.ELEM + Tm.MENU_DROPDOWN_MAIN + At.NOT_PRESENTED
        assert Tm.MENU_DROPDOWN_MAIN in self.browser.find_element(*Mp.MENU_DROPDOWN_MAIN).text, (At.TEXT_IN_ELEM +
        Tm.MENU_DROPDOWN_MAIN + At.NOT_PRESENTED)

    def menu_dropdown_click(self):
        menu_dropdown = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(Mp.MENU_DROPDOWN_MAIN))
        time.sleep(1)
        menu_dropdown.click()

    def should_be_template_mgmt_in_menu(self):
        assert self.is_element_present(*Mp.MENU_TEMPLATES_MGMT), At.ELEM + Tm.MENU_TEMPLATES_MGMT + At.NOT_PRESENTED
        assert Tm.MENU_TEMPLATES_MGMT in self.browser.find_element(*Mp.MENU_TEMPLATES_MGMT).text, (At.TEXT_IN_ELEM +
        Tm.MENU_TEMPLATES_MGMT + At.NOT_PRESENTED)

    def should_be_partners_mgmt_in_menu(self):
        assert self.is_element_present(*Mp.MENU_PARTNERS_MGMT), At.ELEM + Tm.MENU_PARTNERS_MGMT + At.NOT_PRESENTED
        assert Tm.MENU_PARTNERS_MGMT in self.browser.find_element(*Mp.MENU_PARTNERS_MGMT).text, (At.TEXT_IN_ELEM +
        Tm.MENU_PARTNERS_MGMT + At.NOT_PRESENTED)

    def should_be_user_mgmt_in_menu(self):
        assert self.is_element_present(*Mp.MENU_USERS_MGMT), At.ELEM + Tm.MENU_USERS_MGMT + At.NOT_PRESENTED
        assert Tm.MENU_USERS_MGMT in self.browser.find_element(*Mp.MENU_USERS_MGMT).text, (At.TEXT_IN_ELEM +
        Tm.MENU_USERS_MGMT + At.NOT_PRESENTED)

    def should_be_setup_request_in_menu(self):
        assert self.is_element_present(*Mp.MENU_SETUP_SHEET), At.ELEM + Tm.MENU_SETUP_SHEET + At.NOT_PRESENTED
        assert Tm.MENU_SETUP_SHEET in self.browser.find_element(*Mp.MENU_SETUP_SHEET).text, (At.TEXT_IN_ELEM +
        Tm.MENU_SETUP_SHEET + At.NOT_PRESENTED)

    def should_be_logout_btn(self):
        assert self.is_element_present(*Mp.LOGOUT_BTN), At.ELEM + Tm.LOGOUT_BTN + At.NOT_PRESENTED
        assert Tm.LOGOUT_BTN in self.browser.find_element(*Mp.LOGOUT_BTN).text, (At.TEXT_IN_ELEM +
        Tm.LOGOUT_BTN + At.NOT_PRESENTED)

    def logout_btn_click(self):
        logout = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(Mp.LOGOUT_BTN))
        time.sleep(1)
        logout.click()


    # SEARCH block methods started
    def should_be_country_dropdown_header(self):
        assert Tm.COUNTRY_SEARCH in self.browser.find_element(*Mp.COUNTRY_SEARCH).text, (At.TEXT_IN_ELEM +
                                                                        Tm.COUNTRY_SEARCH + At.NOT_PRESENTED)

    def should_be_partner_name_header(self):
        assert Tm.PARTNER_SEARCH in self.browser.find_element(*Mp.PARTNER_SEARCH).text, (At.TEXT_IN_ELEM +
                                                                        Tm.PARTNER_SEARCH + At.NOT_PRESENTED)

    def should_be_category_header(self):
        assert Tm.CATEGORY_SEARCH in self.browser.find_element(*Mp.CATEGORY_SEARCH).text, (At.TEXT_IN_ELEM +
                                                                        Tm.CATEGORY_SEARCH + At.NOT_PRESENTED)

    def should_be_generated_by_header(self):
        assert Tm.GENERATED_BY_SEARCH in self.browser.find_element(*Mp.GENERATED_BY_SEARCH).text, (At.TEXT_IN_ELEM +
                                                                        Tm.GENERATED_BY_SEARCH + At.NOT_PRESENTED)

    # def should_be_search_btn(self):
    #     global search_btn = self.browser.find_element(*Mp.SEARCH_BTN)
    #     assert