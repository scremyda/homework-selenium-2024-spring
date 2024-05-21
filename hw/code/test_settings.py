from ui.pages.settings_page import SettingsPage

from base import BaseCase


class TestSettings(BaseCase):
    INPUT_ADD_ACCOUNT_VK_ID = "123456789"
    
    def test_check_access_redirect(self, settings_page):
        settings_page.open_access_rights()

        assert self.driver.current_url == settings_page.locators.EXPECTED_ACCESS_URL

    def test_check_access_additional_accounts_redirect(self, settings_page):
        settings_page.open_access_rights()

        settings_page.open_access_rights_details()

        settings_page.switch_to_opened_window()
        assert self.driver.current_url == settings_page.locators.EXPECTED_ACCESS_DETAILS_URL

    def test_check_access_add_account(self, settings_page):
        settings_page.open_access_rights()

        settings_page.open_access_rights_add_account()

        assert settings_page.check_opened_add_account_window()

    def test_check_access_add_account_close(self, settings_page):
        settings_page.open_access_rights()

        settings_page.open_access_rights_add_account()

        settings_page.close_access_rights_add_account()

        assert settings_page.check_opened_add_account_window()

    def test_check_access_add_account_id(self, settings_page):
        settings_page.open_access_rights()

        settings_page.open_access_rights_add_account()

        settings_page.write_add_account_id_input(settings_page.get_add_account_window_id_input())

        input_value = settings_page.get_add_account_input(settings_page.get_add_account_window_id_input())

        assert input_value == self.INPUT_ADD_ACCOUNT_VK_ID

    def test_check_access_add_account_id_empty_input(self, settings_page):
        settings_page.open_access_rights()

        settings_page.open_access_rights_add_account()

        settings_page.save_access_rights_add_account()

        assert settings_page.get_add_account_save_error()

    def test_check_access_common_redirect(self, settings_page):
        settings_page.open_access_rights()

        settings_page.open_common()

        assert self.driver.current_url == settings_page.locators.EXPECTED_COMMON_URL

    def test_common_user_language_list(self, settings_page):
        settings_page.scroll_to_about_access()

        settings_page.open_user_language_list()

        assert settings_page.get_user_language_list

    def test_common_redirect_help_api(self, settings_page):
        settings_page.scroll_to_about_access()

        settings_page.open_more_about_access()

        settings_page.switch_to_opened_window()

        assert self.driver.current_url == settings_page.locators.EXPECTED_COMMON_ABOUT_ACCESS_URL

    def test_notifications_redirect(self, settings_page):
        settings_page.open_access_rights()

        settings_page.open_notifications()

        assert self.driver.current_url == settings_page.locators.EXPECTED_NOTIFICATIONS_URL

    def test_notifications_connect_tg_redirect(self, settings_page):
        settings_page.open_notifications()

        settings_page.open_connect_tg()

        settings_page.switch_to_opened_window()

        assert settings_page.locators.EXPECTED_NOTIFICATIONS_CONNECT_TG_URL in self.driver.current_url

    def test_history_of_changes_redirect(self, settings_page):
        settings_page.open_history_of_changes()

        assert self.driver.current_url == settings_page.locators.EXPECTED_CHANGED_HISTORY_URL

    def test_history_of_changes_filter(self, settings_page):
        settings_page.open_history_of_changes()

        settings_page.open_changed_history_filter()

        assert settings_page.get_history_of_changes_filter