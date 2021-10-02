from front_office.login_page import LoginPage
from front_office.reset_password_page import ResetPasswordPage
from data import Urls, Creds
import pytest


@pytest.mark.smoke
def test_user_should_go_to_login_page(browser):
    login_page = LoginPage(browser, Urls.LOGIN_PAGE)
    login_page.open()
    login_page.should_be_login_page()


@pytest.mark.smoke
def test_general_elements_presented_on_login_page(browser):
    login_page = LoginPage(browser, Urls.LOGIN_PAGE)
    login_page.open()
    login_page.email_field_present()
    login_page.password_field_present()
    login_page.remember_me_checkbox_present()
    login_page.login_btn_present()
    login_page.forgot_password_link_present()


@pytest.mark.smoke
def test_user_can_got_to_forgot_pass_link(browser):
    login_page = LoginPage(browser, Urls.LOGIN_PAGE)
    login_page.open()
    login_page.click_forgot_password_link()
    reset_pass_page = ResetPasswordPage(browser, Urls.RESET_PASSWORD)
    reset_pass_page.should_be_reset_pass_url()
    reset_pass_page.should_be_reset_password_text_above_the_form()


@pytest.mark.smoke
def test_user_can_login(browser):
    login_page = LoginPage(browser, Urls.LOGIN_PAGE)
    login_page.open()
    login_page.login_into_system(Creds.LOGIN, Creds.PASSWORD)



