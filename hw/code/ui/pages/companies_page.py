from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class CompaniesPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard/ads'
    locators = basic_locators.CompaniesPageLocators()

    def click_create_btn(self):
        self.find(self.locators.CREATE_BUTTON).click()