from front_office.main_page import MainPage
from front_office.login_page import LoginPage
from data import Urls, Creds
from pages.base_page import BasePage
import pytest
import time


def test_send_function_to_telegram():
    BasePage.send_test_case_to_telegram(f'{test_send_function_to_telegram}')

@pytest.mark.smoke
def test_menu_dropdown_and_elements(browser):
    BasePage.send_test_case_to_telegram(f'{test_menu_dropdown_and_elements}')
    main_page = MainPage(browser, Urls.LOGIN_PAGE)
    main_page.open()
    main_page.login_into_system(Creds.ADMIN_LOGIN, Creds.ADMIN_PASSWORD)
    main_page.should_be_main_page()
    main_page.menu_dropdown_click()
    main_page.should_be_menu_dropdown()
    main_page.should_be_template_mgmt_in_menu()
    main_page.should_be_partners_mgmt_in_menu()
    main_page.should_be_user_mgmt_in_menu()
    main_page.should_be_setup_request_in_menu()

# def test_menu_element_goes_to_theirs_pages(browser):


@pytest.mark.smoke
def test_user_can_logout(browser):
    main_page = MainPage(browser, Urls.LOGIN_PAGE)
    login_page = LoginPage(browser, Urls.LOGIN_PAGE)
    main_page.open()
    main_page.login_into_system(Creds.ADMIN_LOGIN, Creds.ADMIN_PASSWORD)
    main_page.should_be_main_page()
    main_page.should_be_logout_btn()
    main_page.logout_btn_click()
    login_page.should_be_login_text_above_the_form()


@pytest.mark.smoke
def test_search_block_available(browser):
    main_page = MainPage(browser, Urls.LOGIN_PAGE)
    main_page.open()
    main_page.login_into_system(Creds.ADMIN_LOGIN, Creds.ADMIN_PASSWORD)
    main_page.should_be_search_block()


def test_generate_btn_and_table_btns_navigation_available(browser):
    main_page = MainPage(browser, Urls.LOGIN_PAGE)
    main_page.open()
    main_page.login_into_system(Creds.ADMIN_LOGIN, Creds.ADMIN_PASSWORD)
    main_page.should_be_generate_btn()
    main_page.should_be_columns_dropdown()
    main_page.should_be_items_per_page_dropdown()


def test_search_block_elements_can_be_clicked_and_filled(browser):
    main_page = MainPage(browser, Urls.LOGIN_PAGE)
    main_page.open()
    main_page.login_into_system(Creds.ADMIN_LOGIN, Creds.ADMIN_PASSWORD)
    main_page.country_dropdown_click()
    main_page.country_dropdown_sample_element_can_be_selected()

def test_element_presented_on_grid(browser):
    main_page = MainPage(browser, Urls.LOGIN_PAGE)
    main_page.open()
    
