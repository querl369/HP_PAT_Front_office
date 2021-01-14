from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGO_TEXT = (By.CSS_SELECTOR, '.navbar-header .navbar-brand')
    LOGIN_FORM_HEADER = (By.CSS_SELECTOR, 'h3')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[name="LoginForm[email]"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[name="LoginForm[password]"]')
    REMEMBER_BE_CHECKBOX = (By.CSS_SELECTOR, '[type="checkbox"]')
    LOGIN_BTN = (By.CSS_SELECTOR, '[name="login-button"]')
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, '[href="/reset-password-request"]')


class ResetPasswordLocators:
    RESET_PASSWORD_HEADER = (By.CSS_SELECTOR, '.site-request-password-reset>h1')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[name="PasswordResetRequestForm[email]"]')
    SUBMIT_BTN = (By.CSS_SELECTOR, '[type="submit"]')
    WARN_UNREG_USR = (By.CSS_SELECTOR, 'div>p.help-block')


class MainPageLocators:
    GENERATE_FEED_BTN = (By.CSS_SELECTOR, '#import-templates')
