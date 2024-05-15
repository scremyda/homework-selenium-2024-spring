from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class CompaniesPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard/ads'
    locators = basic_locators.CompaniesPageLocators()

    LOW_BUDGET = 10
    CORRECT_BUDGET = 1000
    TARGET_SITE = "ads.vk.com"

    def click_create_btn(self):
        self.find(self.locators.CREATE_BUTTON).click()

    def click_plans_btn(self):
        self.find(self.locators.PLANS_BUTTON).click()

    def click_groups_btn(self):
        self.find(self.locators.GROUPS_BUTTON).click()

    def click_ads_btn(self):
        self.find(self.locators.ADS_BUTTON).click()

    def select_site_target(self):
        self.find(self.locators.SITE_TARGET).click()

    def input_site_value(self, url):
        input = self.find(self.locators.SITE_INPUT)
        input.click()
        input.send_keys(url)
        input.send_keys(Keys.RETURN)

    def input_budget_value(self, budget_value):
        input = self.find(self.locators.BUDGET_INPUT)
        input.click()
        input.send_keys(budget_value)
        input.send_keys(Keys.RETURN)

    def click_contitnue_btn(self):
        self.find(self.locators.CONTINUE_BUTTON).click()

    def create_company(self, url, budget):
        self.click_create_btn()
        self.select_site_target()
        self.input_site_value(url)
        self.input_budget_value(budget)
        self.click_contitnue_btn()

    def select_mobileapp_target(self):
        self.find(self.locators.MOBILEAPP_TARGET).click()

    def get_target_input(self):
        try:
            return self.find(self.locators.TARGET_INPUT)
        except TimeoutException:
            return None
        
    def get_mobile_target_input(self):
        try:
            return self.find(self.locators.MOBILE_TARGET_INPUT)
        except TimeoutException:
            return None
        
    def go_to_root(self):
        self.find(self.locators.ROOT).click()

    def click_drafts_btn(self):
        self.find(self.locators.DRAFTS_BUTTON).click()

    def input_search_query(self, query):
        input = self.find(self.locators.SEARCH_FIELD)
        input.click()
        input.send_keys(query)
