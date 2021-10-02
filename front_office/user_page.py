import time

from pages.base_page import BasePage
from pages.locators import User, TempMail
from data import TextMainPage as Tm, Urls
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UserPage(BasePage):
    def should_be_create_user_page(self):
        assert Urls.USER_CREATE_PAGE in self.browser.current_url, "URL is incorrect"

    def should_be_email_field(self):
        assert User.EMAIL_FIELD, "No Email field displayed"

    def email_field_send_keys(self):
        email_field = self.browser.find_element(*User.EMAIL_FIELD)
        email_field.send_keys(Keys.CONTROL + 'v')

    def should_be_first_name_field(self):
        assert User.FIRST_NAME_FIELD, "No First name field"

    def first_name_send_keys(self):
        first_name = self.browser.find_element(*User.FIRST_NAME_FIELD)
        first_name.send_keys("Test")

    def should_be_last_name_field(self):
        assert User.LAST_NAME_FIELD, "No Last name field displayed"

    def last_name_send_keys(self):
        last_name = self.browser.find_element(*User.LAST_NAME_FIELD)
        last_name.send_keys("User")

    def should_user_role_dropdown(self):
        assert User.USER_ROLE_DROPDOWN, "No User role dropdown displayed"

    def select_user_role(self):
        user_role = self.browser.find_element(*User.USER_ROLE_DROPDOWN)
        user_role.click()
        user_role_select = self.browser.find_element(*User.USER_ROLE_DROPDOWN_SELECT)
        user_role_select.click()

    def should_be_partners_dropdown(self):
        assert User.PARTNERS_DROPDOWN, "No Partners dropdown displayed"

    def select_partner(self):
        partner_field = self.browser.find_element(*User.PARTNERS_DROPDOWN)
        partner_field.click()
        partner_field_select = self.browser.find_element(*User.PARTNERS_DROPDOWN_SELECT)
        partner_field_select.click()
        locale_field = self.browser.find_element(*User.LOCALE_FIELD)
        locale_field.click()
        locale_field_select = self.browser.find_element(*User.LOCALE_SELECT)
        locale_field_select.click()

    def should_be_create_btn(self):
        assert User.CREATE_USER_BTN, "No Create button displayed"

    def create_btn_click(self):
        create_btn = self.browser.find_element(*User.CREATE_USER_BTN)
        create_btn.click()

    def click_to_copy_temp_email(self):
        temp_mail_locate = self.browser.find_element(*TempMail.COPIE_EMAIL)
        temp_mail_locate.click()

    def message_body_to_set_password(self):
        message_body = self.browser.find_element(*TempMail.MESSAGE_BODY)
        message_body.click()

    def message_link(self):
        message_link = self.browser.find_element(*TempMail.LINK_SET_PASSWORD)
        message_link.click()

    def open_new_tab(self):
        self.browser.execute_script("window.open('https://hppat.bintime.com','_blank')")
    def switch_to_new_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    def switch_to_tab_set_password(self):
        self.browser.switch_to.window(self.browser.window_handles[2])

    def switch_to_mail_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[0])

    def switch_to_set_password_window(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    def set_password(self):
        password = self.browser.find_element(*User.SET_PASSWORD)
        password.send_keys("Testuser123")
        confirm_password = self.browser.find_element(*User.CONFIRM_PASSWORD)
        confirm_password.send_keys("Testuser123")

    def save_btn_click(self):
        save_btn = self.browser.find_element(*User.SAVE_BTN)
        save_btn.click()

