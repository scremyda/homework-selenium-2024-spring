import pytest

from contextlib import contextmanager
from typing import Dict
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.pages.base_page import PageNotOpenedExeption


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver: WebDriver, config: Dict, request: FixtureRequest):
        self.driver = driver
        self.config = config

    def is_url_open(self, url, timeout=None):
        if timeout is None:
            timeout = 10
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
            return True
        except:
            raise PageNotOpenedExeption(
                f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')
