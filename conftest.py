from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en', help='Choose language etc"es/ru/ua/fr/de..."')


@pytest.fixture(scope='function')
def browser(request):
    global browser
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        print(f"\nstart chrome browser for test.. with {user_language} language")
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
        print(f"\nstart firefox browser for test.. with {user_language} language")

    yield browser
    print("\nquit browser..")
    browser.quit()
