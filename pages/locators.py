from selenium.webdriver.common.by import By


class LoginPage:
    LOGO_TEXT = (By.CSS_SELECTOR, '.navbar-header .navbar-brand')
    LOGIN_FORM_HEADER = (By.CSS_SELECTOR, 'h3')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[name="LoginForm[email]"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[name="LoginForm[password]"]')
    REMEMBER_BE_CHECKBOX = (By.CSS_SELECTOR, '[type="checkbox"]')
    LOGIN_BTN = (By.CSS_SELECTOR, '[name="login-button"]')
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, '[href="/reset-password-request"]')


class ResetPassword:
    RESET_PASSWORD_HEADER = (By.CSS_SELECTOR, '.site-request-password-reset>h1')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[name="PasswordResetRequestForm[email]"]')
    SUBMIT_BTN = (By.CSS_SELECTOR, '[type="submit"]')
    WARN_UNREG_USR = (By.CSS_SELECTOR, 'div>p.help-block')


class MainPage:
    GENERATE_FEED_BTN = (By.CSS_SELECTOR, '#import-templates')
    MENU_DROPDOWN_MAIN = (By.CSS_SELECTOR, '.dropdown>.dropdown-toggle')
    MENU_TEMPLATES_MGMT = (By.CSS_SELECTOR, '.dropdown.show ul>li:nth-child(1)')
    MENU_PARTNERS_MGMT = (By.CSS_SELECTOR, '.dropdown.show ul>li:nth-child(3)')
    MENU_USERS_MGMT = (By.CSS_SELECTOR, '.dropdown.show ul>li:nth-child(5)')
    MENU_SETUP_SHEET = (By.CSS_SELECTOR, '.dropdown.show ul>li:nth-child(7)')
    LOGOUT_BTN = (By.CSS_SELECTOR, '.logout-link')
    COUNTRY_SEARCH = (By.CSS_SELECTOR, '[for="locales-filter"]')
    COUNTRY_SEARCH_DROPDOWN = (By.CSS_SELECTOR, '[id="select2-requestsearch-locales-container"]')
    PARTNER_SEARCH = (By.CSS_SELECTOR, '[for="name-filter"]')
    PARTNER_SEARCH_FIELD = (By.CSS_SELECTOR, '[name="RequestSearch[name]"]')
    CATEGORY_SEARCH = (By.CSS_SELECTOR, '[for="tags-filter"]')
    CATEGORY_SEARCH_FIELD = (By.CSS_SELECTOR, '[name="RequestSearch[tags]"]')
    GENERATED_BY_SEARCH = (By.CSS_SELECTOR, '[for="userUid-filter"]')
    GENERATED_BY_DROPDOWN = (By.CSS_SELECTOR, '#select2-GeneratedBy-container')
    SEARCH_BTN = (By.CSS_SELECTOR, '.submit.btn.btn-success')
    CLEAR_BTN = (By.CSS_SELECTOR, '.clearFilter.btn.btn-secondary')
    GENERATE_BTN = (By.CSS_SELECTOR, '#import-templates')
    COLUMNS_DROPDOWN = (By.CSS_SELECTOR, '.columnPicker.btn-group>#w2')
    ITEMS_PER_PAGE_DEFAULT = (By.CSS_SELECTOR, '.pageLimiter.btn-group>#w0')
