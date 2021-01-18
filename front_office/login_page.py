from pages.base_page import BasePage
from pages.locators import LoginPage as Lp
from data import TextMainPage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_logo_text()
        self.should_be_login_text_above_the_form()

    def should_be_logo_text(self):
        assert TextMainPage.MAIN_LOGO in self.browser.find_element(*Lp.LOGO_TEXT).text, 'Logo text not present'

    def should_be_login_text_above_the_form(self):
        assert self.is_element_present(*Lp.LOGIN_FORM_HEADER), 'Login form header not present'

    def email_field_present(self):
        assert self.is_element_present(*Lp.EMAIL_FIELD), 'Email field not present'

    def password_field_present(self):
        assert self.is_element_present(*Lp.PASSWORD_FIELD), 'Password field not present'

    def remember_me_checkbox_present(self):
        assert self.is_element_present(*Lp.REMEMBER_BE_CHECKBOX), 'Checkbox not present'

    def login_btn_present(self):
        assert self.is_element_present(*Lp.LOGIN_BTN), 'Login button not present'

    def forgot_password_link_present(self):
        assert self.is_element_present(*Lp.FORGOT_PASSWORD_LINK), "Forgot password link not present"

    def click_remember_me_checkbox(self):
        checkbox = self.browser.find_element(*Lp.REMEMBER_BE_CHECKBOX)
        checkbox.click()

    def click_login_btn(self):
        login_btn = self.browser.find_element(*Lp.LOGIN_BTN)
        login_btn.click()

    def click_forgot_password_link(self):
        forgot_pass_link = self.browser.find_element(*Lp.FORGOT_PASSWORD_LINK)
        forgot_pass_link.click()


