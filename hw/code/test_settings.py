import time
from base import BaseCase
from ui.pages.settings_page import SettingsPage



class TestSettings(BaseCase):
    def test_check_access_redirect(self, settings_page: SettingsPage):
        settings_page.open_settings()

        time.sleep(5)

        settings_page.open_access_rights()

        time.sleep(5)

        assert self.driver.current_url == settings_page.locators.EXPECTED_ACCESS_URL