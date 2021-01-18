from pages.base_page import BasePage
from pages.locators import ResetPassword as RpL


class ResetPasswordPage(BasePage):
    def should_be_reset_pass_url(self):
        assert 'reset-password-request' in self.browser.current_url

    # FIXME: figure out how to get text from disappearing warning
    def cant_reset_unregistered_usr_warn(self):
        assert 'email does not exist' in self.is_element_present(*RpL.WARN_UNREG_USR).text, 'Warn message not present'

    # FIXME: figure out how to get text from disappearing warning
    def should_be_blank_email_warn(self):
        assert 'Email cannot be blank' in self.is_element_present(*RpL.WARN_UNREG_USR).text, ('Blank email message not '
                                                                                              'presented')

    def should_be_reset_password_text_above_the_form(self):
        assert self.is_element_present(*RpL.RESET_PASSWORD_HEADER), '"Request password" text in header not present'

    def email_field_present(self):
        assert self.is_element_present(*RpL.EMAIL_FIELD), 'Email field not present'

    def fill_email_field(self, email):
        email_field = self.browser.find_element(*RpL.EMAIL_FIELD)
        email_field.send_keys(email)

    def send_btn_click(self):
        send_btn = self.browser.find_element(*RpL.SUBMIT_BTN)
        send_btn.click()
