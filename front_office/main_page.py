from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators as MpL
from data import TextPresented as Tp, AssertionText as At, Urls
import time
from selenium.webdriver.common.by import By



class MainPage(BasePage):
    # TODO: write methods to fill test case
    def should_be_main_page(self):
        assert Urls.MAIN_PAGE in self.browser.current_url, 'URL is incorrect'

    # def should_be_menu_and_its_elements(self):
    #     self.should_be_menu_dropdown()
    #     self.menu_dropdown_click()
    #     self.should_be_template_mgmt_in_menu()
    #     self.should_be_partners_mgmt_in_menu()
    #     self.should_be_user_mgmt_in_menu()
    #     self.should_be_setup_request_in_menu()

    def should_be_menu_dropdown(self):
        assert self.is_element_present(*MpL.MENU_DROPDOWN_MAIN), At.ELEM + Tp.MENU_DROPDOWN_MAIN + At.NOT_PRESENTED
        assert Tp.MENU_DROPDOWN_MAIN in self.browser.find_element(*MpL.MENU_DROPDOWN_MAIN).text, (At.TEXT_IN_ELEM +
        Tp.MENU_DROPDOWN_MAIN + At.NOT_PRESENTED)

    def menu_dropdown_click(self):
        menu_dropdown = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(MpL.MENU_DROPDOWN_MAIN))
        time.sleep(1)
        menu_dropdown.click()

    def should_be_template_mgmt_in_menu(self):
        assert self.is_element_present(*MpL.MENU_TEMPLATES_MGMT), At.ELEM + Tp.MENU_TEMPLATES_MGMT + At.NOT_PRESENTED
        assert Tp.MENU_TEMPLATES_MGMT in self.browser.find_element(*MpL.MENU_TEMPLATES_MGMT).text, (At.TEXT_IN_ELEM +
        Tp.MENU_TEMPLATES_MGMT + At.NOT_PRESENTED)

    def should_be_partners_mgmt_in_menu(self):
        assert self.is_element_present(*MpL.MENU_PARTNERS_MGMT), At.ELEM + Tp.MENU_PARTNERS_MGMT + At.NOT_PRESENTED
        assert Tp.MENU_PARTNERS_MGMT in self.browser.find_element(*MpL.MENU_PARTNERS_MGMT).text, (At.TEXT_IN_ELEM +
        Tp.MENU_PARTNERS_MGMT + At.NOT_PRESENTED)

    def should_be_user_mgmt_in_menu(self):
        assert self.is_element_present(*MpL.MENU_USERS_MGMT), At.ELEM + Tp.MENU_USERS_MGMT + At.NOT_PRESENTED
        assert Tp.MENU_USERS_MGMT in self.browser.find_element(*MpL.MENU_USERS_MGMT).text, (At.TEXT_IN_ELEM +
        Tp.MENU_USERS_MGMT + At.NOT_PRESENTED)

    def should_be_setup_request_in_menu(self):
        assert self.is_element_present(*MpL.MENU_SETUP_SHEET), At.ELEM + Tp.MENU_SETUP_SHEET + At.NOT_PRESENTED
        assert Tp.MENU_SETUP_SHEET in self.browser.find_element(*MpL.MENU_SETUP_SHEET).text, (At.TEXT_IN_ELEM +
        Tp.MENU_SETUP_SHEET + At.NOT_PRESENTED)

    def should_be_logout_btn(self):
        assert self.is_element_present(*MpL.LOGOUT_BTN), At.ELEM + Tp.LOGOUT_BTN + At.NOT_PRESENTED
        assert Tp.LOGOUT_BTN in self.browser.find_element(*MpL.LOGOUT_BTN).text, (At.TEXT_IN_ELEM +
        Tp.LOGOUT_BTN + At.NOT_PRESENTED)

    def logout_btn_click(self):
        logout = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(MpL.LOGOUT_BTN))
        time.sleep(1)
        logout.click()


    # def dropdown_menu_is_selectable(self):
    #
    #
    # def search_fields_checked(self):
    #
    #
    #
    # def country_dropdown_text_presented(self):
