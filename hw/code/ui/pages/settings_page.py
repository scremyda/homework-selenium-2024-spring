import time

from selenium.common.exceptions import TimeoutException

from ui.locators.settings_locators import SettingsPageLocators
from ui.pages.base_page import BasePage


class SettingsPage(BasePage):
    url = 'https://ads.vk.com/hq/settings'
    locators = SettingsPageLocators()

    def open_settings(self):
        self.click(self.locators.OPEN_SETTINGS)

    def find_header_accounts(self):
        return self.scroll_until_element_found(self.locators.HEADER_ACCOUNTS)

    def find_header_access(self):
        return self.scroll_until_element_found(self.locators.HEADER_ACCESS)

    def find_header_change_access(self):
        return self.scroll_until_element_found(self.locators.HEADER_CHANGE_ACCESS)

    def find_header_other_accounts_access(self):
        return self.scroll_until_element_found(self.locators.HEADER_OTHER_ACCOUNTS_ACCESS)

    def get_access_accounts(self):
        return self.find(self.locators.TEXT_ACCESS_ACCOUNTS)

    def get_button_add_accounts(self):
        return self.find(self.locators.BUTTON_ADD_ACCOUNTS)

    def get_details_link(self):
        return self.find(self.locators.LINK_DETAILS)

    def get_extended_rights_access_companies(self):
        return self.find(self.locators.ACCESS_COMPANIES)

    def get_extended_rights_access_money(self):
        return self.find(self.locators.ACCESS_MONEY)

    def get_only_read_access_companies(self):
        return self.find(self.locators.ACCESS_COMPANIES)

    def get_only_read_rights_access_money(self):
        return self.find(self.locators.ACCESS_MONEY)


    def open_access_rights(self):
        self.click(self.locators.OPEN_ACCESS_RIGHTS)

    def open_history_of_changes(self):
        self.click(self.locators.OPEN_HISTORY_OF_CHANGES)

    def open_changed_history_filter(self):
        self.click(self.locators.OPEN_HISTORY_OF_CHANGES_FILTER)

    def open_access_rights_details(self):
        self.click(self.locators.OPEN_ACCESS_RIGHTS_DETAILS)

    def open_access_rights_add_account(self):
        self.click(self.locators.OPEN_ACCESS_RIGHTS_ADD_ACCOUNT)

    def open_extended_access(self):
        self.click(self.locators.OPEN_EXTENDED_RIGHTS)


    def close_access_rights_add_account(self):
        self.click(self.locators.CLOSE_ACCESS_RIGHTS_ADD_ACCOUNT)

    def check_opened_add_account_window(self) -> bool:
        return self.became_visible(self.locators.WINDOW_ACCESS_RIGHTS_ADD_ACCOUNT)

    def get_add_account_window_id_input(self):
        return self.find(self.locators.WINDOW_ACCESS_RIGHTS_ADD_ACCOUNT_ID)

    def write_add_account_id_input(self, input_vk_id):
        input_vk_id.send_keys(self.locators.INPUT_ADD_ACCOUNT_VK_ID)

    def get_add_account_input(self, input_vk_id):
        return input_vk_id.get_attribute(self.locators.INPUT_ATTRIBUTE)

    def get_add_account_save_error(self):
        return self.find(self.locators.WINDOW_ACCESS_RIGHTS_ADD_ACCOUNT_ID_ERROR)

    def save_access_rights_add_account(self):
        self.click(self.locators.WINDOW_ACCESS_RIGHTS_ADD_ACCOUNT_ID_SAVE)

    def open_common(self):
        self.click(self.locators.OPEN_COMMON)

    def open_notifications(self):
        self.click(self.locators.OPEN_NOTIFICATIONS)

    def open_connect_tg(self):
        self.click(self.locators.OPEN_CONNECT_TG)

    def open_user_language_list(self):
        self.click(self.locators.OPEN_USER_LANGUAGE_LIST)

    def open_more_about_access(self):
        self.click(self.locators.OPEN_MORE_ABOUT_ACCESS)

    def scroll_to_about_access(self):
        self.scroll_to_element(self.locators.OPEN_MORE_ABOUT_ACCESS)

    def get_user_language_list(self):
        return self.find(self.locators.USER_LANGUAGE_LIST)

    def get_history_of_changes_filter(self):
        return self.find(self.locators.HISTORY_FILTER)

    def switch_to_opened_window(self, timeout = 10):
        window_handles = self.driver.window_handles

        start_time = time.time()
        while len(window_handles) == 1:
            if time.time() - start_time > timeout:
                raise TimeoutException
            window_handles = self.driver.window_handles

        new_window_handle = window_handles[-1]
        self.driver.switch_to.window(new_window_handle)
