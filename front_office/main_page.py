
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import TextMainPage as Tm, Urls
from pages.base_page import BasePage
from pages.locators import MainPage as Mp


class MainPage(BasePage):

    """ MAIN elements on the page"""
    def should_be_main_page(self):
        assert Urls.MAIN_PAGE in self.browser.current_url, 'URL is incorrect'

    def should_be_search_btn(self):
        assert self.text_assert(*Mp.SEARCH_BTN), self.no_text(Tm.SEARCH_BTN)
        assert self.is_element_present(*Mp.SEARCH_BTN), self.no_elem(Tm.SEARCH_BTN)

    def click_search_btn(self):
        search_btn = self.browser.find_element(*Mp.SEARCH_BTN)
        search_btn.click()

    def should_be_clear_btn(self):
        assert self.is_element_present(*Mp.CLEAR_BTN), self.no_elem(Tm.CLEAR_BTN)
        assert self.text_assert(*Mp.CLEAR_BTN), self.no_text(Tm.CLEAR_BTN)

    def click_clear_btn(self):
        clear_btn = self.browser.find_element(*Mp.CLEAR_BTN)
        clear_btn.click()

    def should_be_columns_dropdown(self):
        assert self.is_element_present(*Mp.COLUMNS_DROPDOWN), self.no_elem(Tm.COLUMNS_DROPDOWN)
        assert self.text_assert(*Mp.COLUMNS_DROPDOWN), self.no_text(Tm.COLUMNS_DROPDOWN)

    def should_be_items_per_page_dropdown(self):
        assert self.is_element_present(*Mp.ITEMS_PER_PAGE_DEFAULT), self.no_elem(Tm.ITEMS_PER_PAGE_DEFAULT)
        assert self.text_assert(*Mp.ITEMS_PER_PAGE_DEFAULT), self.no_text(Tm.ITEMS_PER_PAGE_DEFAULT)
        # print(self.text_assert(*Mp.ITEMS_PER_PAGE_DEFAULT))

    """------------------------------------"""
    """ MENU dropdown methods block started"""
    """------------------------------------"""

    def should_be_menu_dropdown(self):
        assert self.is_element_present(*Mp.MENU_DROPDOWN_MAIN), self.no_elem(Tm.MENU_DROPDOWN_MAIN)
        assert self.text_assert(*Mp.MENU_DROPDOWN_MAIN), self.no_text(Tm.MENU_DROPDOWN_MAIN)

    def menu_dropdown_click(self):
        menu_dropdown = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(Mp.MENU_DROPDOWN_MAIN))
        menu_dropdown.click()

    def should_be_template_mgmt_in_menu(self):
        assert self.is_element_present(*Mp.MENU_TEMPLATES_MGMT), self.no_elem(Tm.MENU_TEMPLATES_MGMT)
        assert self.text_assert(*Mp.MENU_TEMPLATES_MGMT), self.no_text(Tm.MENU_TEMPLATES_MGMT)

    def should_be_partners_mgmt_in_menu(self):
        assert self.is_element_present(*Mp.MENU_PARTNERS_MGMT), self.no_elem(Tm.MENU_PARTNERS_MGMT)
        assert self.text_assert(*Mp.MENU_PARTNERS_MGMT), self.no_text(Tm.MENU_PARTNERS_MGMT)

    def should_be_user_mgmt_in_menu(self):
        assert self.is_element_present(*Mp.MENU_USERS_MGMT), self.no_elem(Tm.MENU_USERS_MGMT)
        assert self.text_assert(*Mp.MENU_USERS_MGMT), self.no_text(Tm.MENU_USERS_MGMT)

    def should_be_setup_request_in_menu(self):
        assert self.is_element_present(*Mp.MENU_SETUP_SHEET), self.no_elem(Tm.MENU_SETUP_SHEET)
        assert self.text_assert(*Mp.MENU_SETUP_SHEET), self.no_text(Tm.MENU_SETUP_SHEET)

    def should_be_logout_btn(self):
        assert self.is_element_present(*Mp.LOGOUT_BTN), self.no_elem(Tm.LOGOUT_BTN)
        assert self.text_assert(*Mp.LOGOUT_BTN), self.no_text(Tm.LOGOUT_BTN)

    def logout_btn_click(self):
        logout = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(Mp.LOGOUT_BTN))
        logout.click()

    """-----------------------------------------"""
    """SEARCH BLOCK METHODS STARTED ON MAIN PAGE"""
    """-----------------------------------------"""

    def should_be_search_block(self):
        self.should_be_country_dropdown()
        self.should_be_partner_name_field()
        self.should_be_category_field()
        self.should_be_generated_by_dropdown()
        self.should_be_search_btn()
        self.should_be_clear_btn()

    def should_be_country_dropdown(self):
        assert self.text_assert(*Mp.COUNTRY_SEARCH), self.no_text(Tm.COUNTRY_SEARCH)
        assert self.is_element_present(*Mp.COUNTRY_SEARCH_DROPDOWN), self.no_elem(Tm.COUNTRY_SEARCH_DROPDOWN)

    def country_dropdown_click(self):
        country_dropdown = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(Mp.COUNTRY_SEARCH_DROPDOWN))
        country_dropdown.click()


    def should_be_partner_name_field(self):
        assert self.text_assert(*Mp.PARTNER_SEARCH), self.no_text(Tm.PARTNER_SEARCH)
        assert self.is_element_present(*Mp.PARTNER_SEARCH_FIELD), self.no_elem(Tm.PARTNER_SEARCH_FIELD)

    def should_be_category_field(self):
        assert self.text_assert(*Mp.CATEGORY_SEARCH), self.no_text(Tm.CATEGORY_SEARCH)
        assert self.is_element_present(*Mp.CATEGORY_SEARCH_FIELD), self.no_elem(Tm.CATEGORY_SEARCH_FIELD)

    def should_be_generated_by_dropdown(self):
        assert self.text_assert(*Mp.GENERATED_BY_SEARCH), self.no_text(Tm.GENERATED_BY_SEARCH)
        assert self.is_element_present(*Mp.GENERATED_BY_DROPDOWN), self.no_elem(Tm.GENERATED_BY_DROPDOWN)
        print(self.text_assert(*Mp.GENERATED_BY_SEARCH))

    def should_be_generate_btn(self):
        assert self.is_element_present(*Mp.GENERATE_BTN), self.no_elem(Tm.GENERATE_BTN)

    def country_dropdown_sample_element_can_be_selected(self):
        list_of_countries = self.browser.find_element(*Mp.COUNTRY_SEARCH_HTML_LIST)
        all_countries = list_of_countries.find_elements(*Mp.COUNTRY_SEARCH_ITEMS)
        new_list = [country.text for country in all_countries]
        print(new_list)
        assert len(new_list) > 1, 'Country dropdown is empty'




