from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class CompaniesPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard/ads'
    locators = basic_locators.CompaniesPageLocators()

    LOW_BUDGET = 10
    CORRECT_BUDGET = 1000
    TARGET_SITE = "ads.vk.com"

    def skip_help(self):
        try:
            self.click(self.locators.SKIP_HELP_BUTTON)
            self.click(self.locators.SKIP_HELP_STEP)
        except TimeoutException:
            pass


    def click_create_btn(self):
        self.click(self.locators.CREATE_BUTTON, 20)

    def click_plans_btn(self):
        self.click(self.locators.PLANS_BUTTON)

    def click_groups_btn(self):
        self.click(self.locators.GROUPS_BUTTON)

    def click_ads_btn(self):
        self.click(self.locators.ADS_BUTTON)

    def select_site_target(self):
        self.click(self.locators.SITE_TARGET)

    def input_site_value(self, url):
        self.became_visible(self.locators.SITE_INPUT)
        input = self.find(self.locators.SITE_INPUT)
        input.clear()
        input.send_keys(url)
        input.send_keys(Keys.ENTER)

    def input_budget_value(self, budget_value):
        self.became_visible(self.locators.BUDGET_INPUT)
        input = self.find(self.locators.BUDGET_INPUT)
        input.clear()
        input.send_keys(budget_value)
        input.send_keys(Keys.ENTER)

    def click_contitnue_btn(self):
        self.scroll_and_click(self.locators.CONTINUE_BUTTON)

    def click_companies_menu_btn(self):
        self.scroll_and_click(self.locators.COMPANIES_MENU_BUTTON)

    def click_save_draft_btn(self):
        self.scroll_and_click(self.locators.SAVE_DRAFT_BUTTON)

    def create_company(self, url, budget):
        self.click_create_btn()
        self.select_site_target()
        self.input_site_value(url)
        self.input_budget_value(budget)
        self.click_contitnue_btn()

    def select_mobileapp_target(self):
        self.click(self.locators.MOBILEAPP_TARGET)

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
        self.click(self.locators.ROOT)

    def click_drafts_btn(self):
        self.click(self.locators.DRAFTS_BUTTON)

    def input_search_query(self, query):
        input = self.find(self.locators.SEARCH_FIELD)
        input.clear()
        input.send_keys(query)
        input.send_keys(Keys.ENTER)

    def find_no_result(self) -> bool:
        return self.became_visible(self.locators.NO_RESULT)