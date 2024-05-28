import time

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from ui.locators import basic_locators


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    locators = basic_locators.BasePageLocators()
    url = 'https://ads.vk.com/'

    def is_opened(self, timeout=30):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url.startswith(self.url):
                return True
        raise PageNotOpenedExeption(
            f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver: RemoteWebDriver):
        self.driver = driver
        self.is_opened()

        self.close_cookie_banner()

    def close_cookie_banner(self):
        try:
            self.click(self.locators.COOKIE_BANNER_BUTTON)
        except:
            pass

    def wait(self, timeout: float | None = 10):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout: float | None = 10, cond=EC.visibility_of_element_located) -> WebElement:
        return self.wait(timeout).until(cond(locator))

    def click(self, locator, timeout: float | None = 10) -> WebElement:
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))

        elem.click()

        return elem

    def wait_for_modal(self, locator, timeout: float | None = 10):
        try:
            add_room_modal = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return add_room_modal
        except TimeoutException:
            return None

    def scroll_until_element_found(self, xpath):

        try:
            element = self.find(xpath)
            return element
        except Exception:
            pass

        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
            last_height = new_height

        try:
            element = self.find(xpath)
            return element
        except Exception:
            return None

    def clear(self, locator, timeout: float | None = 10) -> WebElement:
        elem = self.find(locator, timeout)
        elem.clear()

        if elem.get_attribute('value') != '':
            size = len(elem.get_attribute('value'))
            elem.send_keys(size * Keys.BACKSPACE)

        return elem

    def fill_in(self, locator, query: str, timeout: float | None = 10) -> WebElement:
        elem = self.clear(locator, timeout)
        elem.send_keys(query)
        return elem

    def is_enabled(self, locator, timeout=10) -> bool:
        elem = self.find(locator, timeout=timeout)
        return elem.is_enabled()

    def scroll_to_element(self, element_locator, timeout: float | None = 10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(element_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_and_click(self, locator, timeout=10) -> WebElement:
        elem = self.wait(timeout).until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        return elem

    def became_visible(self, locator, timeout=10) -> bool:
        try:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False