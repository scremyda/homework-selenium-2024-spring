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

    def check_opened_modal_window(self):
        self.wait_for_modal(self.locators.WINDOW_ACCESS_RIGHTS_ADD_ACCOUNT)


    def switch_to_opened_window(self):
        window_handles = self.driver.window_handles

        new_window_handle = window_handles[-1]
        self.driver.switch_to.window(new_window_handle)
