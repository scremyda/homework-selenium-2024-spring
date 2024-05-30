import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from ui.pages.base_page import BasePage
from ui.pages.surveys_page import SurveysPage
from ui.pages.settings_page import SettingsPage
from ui.pages.companies_page import CompaniesPage
from ui.pages.registration_page import RegistrationMainPage, RegistrationPage


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']

    if selenoid:
        options = Options()
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        options.default_capabilities = capabilities

        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub', options=options)
    else:
        match browser:
            case 'chrome':
                driver = webdriver.Chrome()
            case 'firefox':
                driver = webdriver.Firefox()
            case _:
                raise RuntimeError(f'Unsupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def registration_main_page(driver):
    driver.get(RegistrationMainPage.url)
    return RegistrationMainPage(driver=driver)


@pytest.fixture(scope='session')
def load_env():
    load_dotenv('.env')


@pytest.fixture(scope='session')
def credentials(load_env):
    return (os.getenv("LOGIN"), os.getenv("PASSWORD"))


@pytest.fixture
def serveys_page(registration_main_page, credentials):
    registration_main_page.login(*credentials)
    return SurveysPage(registration_main_page.driver)


@pytest.fixture
def settings_page(serveys_page):
    serveys_page.driver.get(SettingsPage.url)
    return SettingsPage(serveys_page.driver)


@pytest.fixture
def companies_page(self):
    self.driver.get(CompaniesPage.url)
    return CompaniesPage(self.driver)

@pytest.fixture
def audience_page(self):
    self.driver.get(AudiencePagePage.url)
    return AudiencePagePage(self.driver)