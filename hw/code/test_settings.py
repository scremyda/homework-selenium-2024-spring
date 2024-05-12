import time
from base import BaseCase
from ui.pages.settings_page import SettingsPage



class TestSettings(BaseCase):
    INPUT_ADD_ACCOUNT_VK_ID = "123456789"

    def test_check_access_redirect(self, settings_page: SettingsPage):
        settings_page.open_settings()

        time.sleep(2)
        settings_page.open_access_rights()

        time.sleep(2)
        assert self.driver.current_url == settings_page.locators.EXPECTED_ACCESS_URL

    def test_check_access_additional_accounts_redirect(self, settings_page: SettingsPage):
        settings_page.open_settings()

        time.sleep(2)
        settings_page.open_access_rights()

        time.sleep(2)
        settings_page.open_access_rights_details()

        time.sleep(2)
        settings_page.switch_to_opened_window()
        assert self.driver.current_url == settings_page.locators.EXPECTED_ACCESS_DETAILS_URL

    def test_check_access_add_account(self, settings_page: SettingsPage):
        settings_page.open_settings()

        time.sleep(2)
        settings_page.open_access_rights()

        time.sleep(2)
        settings_page.open_access_rights_add_account()

        time.sleep(2)
        assert settings_page.check_opened_add_account_window() is not None

    def test_check_access_add_account_close(self, settings_page: SettingsPage):
        settings_page.open_settings()

        time.sleep(2)
        settings_page.open_access_rights()

        time.sleep(2)
        settings_page.open_access_rights_add_account()

        time.sleep(2)
        settings_page.close_access_rights_add_account()

        time.sleep(2)
        assert settings_page.check_opened_add_account_window() is None

    def test_check_access_add_account_id(self, settings_page: SettingsPage):
        settings_page.open_settings()

        time.sleep(2)
        settings_page.open_access_rights()

        time.sleep(2)
        settings_page.open_access_rights_add_account()

        time.sleep(2)
        settings_page.write_add_account_id_input(settings_page.get_add_account_window_id_input())

        input_value = settings_page.get_add_account_input(settings_page.get_add_account_window_id_input())

        time.sleep(2)
        assert input_value == self.INPUT_ADD_ACCOUNT_VK_ID

    def test_check_access_add_account_id_empty_input(self, settings_page: SettingsPage):
        settings_page.open_settings()

        time.sleep(2)
        settings_page.open_access_rights()

        time.sleep(2)
        settings_page.open_access_rights_add_account()

        time.sleep(2)
        settings_page.save_access_rights_add_account()

        time.sleep(2)
        assert settings_page.get_add_account_save_error() is not None


    def test_check_access_common_redirect(self, settings_page: SettingsPage):
        settings_page.open_settings()

        time.sleep(2)
        settings_page.open_access_rights()

        time.sleep(2)
        settings_page.open_common()

        time.sleep(2)
        assert self.driver.current_url == settings_page.locators.EXPECTED_COMMON_URL
