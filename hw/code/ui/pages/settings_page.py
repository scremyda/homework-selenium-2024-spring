from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class SettingsPage(BasePage):
    url = 'https://ads.vk.com/hq/settings'
    locators = basic_locators.SettingsPageLocators()

    def open_settings(self):
        self.click(self.locators.OPEN_SETTINGS)

    def open_access_rights(self):
        self.click(self.locators.OPEN_ACCESS_RIGHTS)
