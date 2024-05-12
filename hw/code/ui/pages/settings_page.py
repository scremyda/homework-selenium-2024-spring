from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class SettingsPage(BasePage):
    url = 'https://ads.vk.com/hq/settings'
    locators = basic_locators.SettingsPageLocators()

    def open_settings(self):
        self.click(self.locators.OPEN_SETTINGS)

    def open_access_rights(self):
        self.click(self.locators.OPEN_ACCESS_RIGHTS)

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

    def switch_to_opened_window(self):
        window_handles = self.driver.window_handles

        new_window_handle = window_handles[-1]
        self.driver.switch_to.window(new_window_handle)
