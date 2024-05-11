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

    def test_check_access_additional_accounts_redirect(self, settings_page: SettingsPage):
        settings_page.open_settings()

        time.sleep(5)
        settings_page.open_access_rights()

        time.sleep(5)
        settings_page.open_access_rights_details()

        time.sleep(5)
        settings_page.switch_to_opened_window()
        assert self.driver.current_url == settings_page.locators.EXPECTED_ACCESS_DETAILS_URL

    # def test_check_access_add_account(self, settings_page: SettingsPage):
    #     settings_page.open_settings()
    #
    #     time.sleep(5)
    #     settings_page.open_access_rights()
    #
    #     time.sleep(5)
    #     settings_page.open_access_rights_add_account()
    #
    #
    #     time.sleep(5)
    #     assert settings_page.check_opened_modal_window() is not None