from pages.base_page import BasePage
from pages.locators import LoginPageLocators as LpL


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_logo_text()
        self.should_be_login_text_above_the_form()

    def should_be_logo_text(self):
        assert 'HP Partner Automation Tool' in self.browser.find_element(*LpL.LOGO_TEXT).text, 'Logo text not present'

    def should_be_login_text_above_the_form(self):
        assert self.is_element_present(*LpL.LOGIN_FORM_HEADER), 'Login form header not present'

    def email_field_present(self):
        assert self.is_element_present(*LpL.EMAIL_FIELD), 'Email field not present'

    def password_field_present(self):
        assert self.is_element_present(*LpL.PASSWORD_FIELD), 'Password field not present'

    def remember_me_checkbox_present(self):
        assert self.is_element_present(*LpL.REMEMBER_BE_CHECKBOX), 'Checkbox not present'

    def login_btn_present(self):
        assert self.is_element_present(*LpL.LOGIN_BTN), 'Login button not present'

    def forgot_password_link_present(self):
        assert self.is_element_present(*LpL.FORGOT_PASSWORD_LINK), "Forgot password link not present"

    # FIXME: Login user process moved to the base_page
    def fill_email_field(self, email='bintime@bintime.com'):
        email_field = self.browser.find_element(*LpL.EMAIL_FIELD)
        email_field.send_keys(email)

    # FIXME: Login user process moved to the base_page
    def fill_password_field(self, password=''):
        pass_field = self.browser.find_element(*LpL.PASSWORD_FIELD)
        pass_field.send_keys(password)

    def click_remember_me_checkbox(self):
        checkbox = self.browser.find_element(*LpL.REMEMBER_BE_CHECKBOX)
        checkbox.click()

    def click_login_btn(self):
        login_btn = self.browser.find_element(*LpL.LOGIN_BTN)
        login_btn.click()

    def click_forgot_password_link(self):
        forgot_pass_link = self.browser.find_element(*LpL.FORGOT_PASSWORD_LINK)
        forgot_pass_link.click()


