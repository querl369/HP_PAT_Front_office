from front_office.reset_password_page import ResetPasswordPage
from data import Urls, Creds
import pytest


@pytest.mark.smoke
def test_user_can_go_to_reset_pass_page(browser):
    reset_pass_page = ResetPasswordPage(browser, Urls.RESET_PASSWORD)
    reset_pass_page.open()
    reset_pass_page.should_be_reset_pass_url()
    reset_pass_page.should_be_reset_password_text_above_the_form()


@pytest.mark.regression
def test_unregistered_user_cant_reset_password(browser):
    reset_pass_page = ResetPasswordPage(browser, Urls.RESET_PASSWORD)
    reset_pass_page.open()
    reset_pass_page.fill_email_field(Creds.SAMPLE_USER_EMAIL)
    reset_pass_page.send_btn_click()
    reset_pass_page.cant_reset_unregistered_usr_warn()


@pytest.mark.regression
def test_form_cant_be_sent_empty(browser):
    reset_pass_page = ResetPasswordPage(browser, Urls.RESET_PASSWORD)
    reset_pass_page.open()
    reset_pass_page.send_btn_click()
    reset_pass_page.should_be_blank_email_warn()
