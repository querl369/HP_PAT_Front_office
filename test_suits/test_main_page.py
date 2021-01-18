from front_office.main_page import MainPage
from front_office.login_page import LoginPage
from data import Urls, Creds
import pytest


@pytest.mark.smoke
def test_menu_dropdown_and_elements(browser):
    main_page = MainPage(browser, Urls.LOGIN_PAGE)
    main_page.open()
    main_page.login_into_system(Creds.ADMIN_LOGIN, Creds.ADMIN_PASSWORD)
    main_page.menu_dropdown_click()
    main_page.should_be_menu_dropdown()
    main_page.should_be_template_mgmt_in_menu()
    main_page.should_be_partners_mgmt_in_menu()
    main_page.should_be_user_mgmt_in_menu()
    main_page.should_be_setup_request_in_menu()


@pytest.mark.smoke
def test_user_can_logout(browser):
    main_page = MainPage(browser, Urls.LOGIN_PAGE)
    login_page = LoginPage(browser, Urls.LOGIN_PAGE)
    main_page.open()
    main_page.login_into_system(Creds.ADMIN_LOGIN, Creds.ADMIN_PASSWORD)
    main_page.should_be_logout_btn()
    main_page.logout_btn_click()
    login_page.should_be_login_text_above_the_form()


