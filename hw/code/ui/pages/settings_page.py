import time

from selenium.common.exceptions import TimeoutException

from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class SettingsPage(BasePage):
    url = 'https://ads.vk.com/hq/settings'
    locators = basic_locators.SettingsPageLocators()

    def open_settings(self):
        self.click(self.locators.OPEN_SETTINGS)

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

    def close_access_rights_add_account(self):
        self.click(self.locators.CLOSE_ACCESS_RIGHTS_ADD_ACCOUNT)

    def check_opened_add_account_window(self):
        return self.wait_for_modal(self.locators.WINDOW_ACCESS_RIGHTS_ADD_ACCOUNT)

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
