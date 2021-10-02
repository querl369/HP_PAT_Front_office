
from front_office.login_page import LoginPage
from front_office.user_page import UserPage
from data import Urls, Creds
import time
from pages.base_page import BasePage

def test_all_fields_available(browser):
    login_page = LoginPage(browser, Urls.LOGIN_PAGE)
    login_page.open()
    login_page.login_into_system(Creds.LOGIN, Creds.PASSWORD)
    fields_check = UserPage(browser, Urls.USER_CREATE_PAGE)
    time.sleep(1)
    fields_check.open()
    fields_check.should_be_create_user_page()
    fields_check.should_be_email_field()
    fields_check.should_be_first_name_field()
    fields_check.should_be_last_name_field()
    fields_check.should_user_role_dropdown()
    fields_check.should_be_partners_dropdown()
    fields_check.should_be_create_btn()

def test_user_can_register(browser):
    temp_mail_page = UserPage(browser, Urls.TEMP_MAIL)
    temp_mail_page.open()
    temp_mail_page.click_to_copy_temp_email()
    temp_mail_page.open_new_tab()
    temp_mail_page.switch_to_new_tab()
    login_page = LoginPage(browser, Urls.LOGIN_PAGE)
    login_page.open()
    login_page.login_into_system(Creds.LOGIN, Creds.PASSWORD)
    user_create_page = UserPage(browser, Urls.USER_CREATE_PAGE)
    user_create_page.open()
    user_create_page.email_field_send_keys()
    user_create_page.first_name_send_keys()
    user_create_page.last_name_send_keys()
    user_create_page.select_user_role()
    user_create_page.select_partner()
    user_create_page.create_btn_click()
    user_create_page.switch_to_mail_tab()
    user_create_page.message_body_to_set_password()
    user_create_page.message_link()
    user_create_page.switch_to_tab_set_password()
    user_create_page.set_password()
    user_create_page.save_btn_click()

