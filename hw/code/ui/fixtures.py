import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.base_page import BasePage
from ui.pages.overview_page import OverviewPage
from ui.pages.settings_page import SettingsPage
from ui.pages.companies_page import CompaniesPage
from ui.pages.registration_page import RegistrationMainPage, RegistrationPage
from dotenv import load_dotenv


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
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
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
def hq_page(registration_main_page, credentials):
    registration_main_page.login(*credentials)
    return OverviewPage(registration_main_page.driver)


@pytest.fixture
def settings_page(hq_page):
    hq_page.driver.get(SettingsPage.url)
    return SettingsPage(hq_page.driver)

@pytest.fixture
def companies_page(hq_page):
    hq_page.driver.get(CompaniesPage.url)
    return CompaniesPage(hq_page.driver)