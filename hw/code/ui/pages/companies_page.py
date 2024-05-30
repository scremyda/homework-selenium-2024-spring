from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from ui.locators.companies_locators import CompaniesPageLocators
from ui.pages.base_page import BasePage

class CompaniesPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard/ads'
    locators = CompaniesPageLocators()

    LOW_BUDGET = 10
    HIGH_BUDGET = 1000
    TARGET_SITE = "ads.vk.com"

    NEED_FIELD_ALERT = "Обязательное поле"
    LOW_BUDGET_ALERT = "Бюджет кампании должен быть не меньше 100₽"

    def skip_help(self):
        try:
            self.click(self.locators.SKIP_HELP_BUTTON)
            self.click(self.locators.SKIP_HELP_STEP)
        except TimeoutException:
            pass
    
    def is_visible_create_company_btn(self) -> bool:
        return self.became_visible(self.locators.CREATE_BUTTON)

    def click_create_company_btn(self):
        self.click(self.locators.CREATE_BUTTON)

    def click_plans_btn(self):
        self.click(self.locators.PLANS_BUTTON)

    def click_groups_btn(self):
        self.click(self.locators.GROUPS_BUTTON)

    def click_ads_btn(self):
        self.click(self.locators.ADS_BUTTON)

    def is_visible_site_target(self) -> bool:
        return self.became_visible(self.locators.SITE_TARGET)

    def select_site_target(self):
        self.click(self.locators.SITE_TARGET)

    def is_visible_input_site(self) -> bool:
        return self.became_visible(self.locators.SITE_INPUT)

    def input_site_value(self, url):
        input = self.find(self.locators.SITE_INPUT)
        input.clear()
        input.send_keys(url)
        input.send_keys(Keys.ENTER)

    def is_visible_input_budget(self) -> bool:
        return self.became_visible(self.locators.BUDGET_INPUT)

    def input_budget_value(self, budget_value):
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

    def scroll_and_click_companies_menu_btn(self):
        self.scroll_and_click(self.locators.COMPANIES_MENU_BUTTON)

    def is_visible_second_step(self) -> bool:
        return self.became_visible(self.locators.SAVE_DRAFT_BUTTON)

    def is_visible_save_draft_status(self) -> bool:
        return self.became_visible(self.locators.SAVE_DRAFT_STATUS)
    
    def is_visible_no_result(self) -> bool:
        return self.became_visible(self.locators.NO_RESULT)

    def is_visible_target_site_input(self) -> bool:
        return self.became_visible(self.locators.SITE_INPUT)

    def is_visible_mobile_target_input(self) -> bool:
        return self.became_visible(self.locators.MOBILE_TARGET_INPUT)

    def is_visible_mobileapp_target(self) -> bool:
        return self.became_visible(self.locators.MOBILEAPP_TARGET)

    def select_mobileapp_target(self):
        self.click(self.locators.MOBILEAPP_TARGET)

    def get_alert(self) -> str:
        return self.find(self.locators.ALERT).text
        
    def go_to_root(self):
        self.click(self.locators.ROOT)

    def click_drafts_btn(self):
        self.click(self.locators.DRAFTS_BUTTON)

    def is_visible_drafts_btn(self) -> bool:
        return self.became_visible(self.locators.DRAFTS_BUTTON)

    def is_visible_enter_search_query(self) -> bool:
        return self.became_visible(self.locators.SEARCH_FIELD)

    def enter_search_query(self, query: str):
        input = self.find(self.locators.SEARCH_FIELD)
        input.clear()
        input.send_keys(query)
        input.send_keys(Keys.ENTER)

    def is_visible_warning_min_length(self) -> bool:
        return self.became_visible(self.locators.WARNING_MIN_LENGTH)

    def is_visible_filter_save_button(self) -> bool:
        return self.became_visible(self.locators.FILTER_SAVE_BUTTON)

    def click_filter_save_button(self):
        self.click(self.locators.FILTER_SAVE_BUTTON)

    def is_visible_filter_save_modal_button(self) -> bool:
        return self.became_visible(self.locators.FILTER_SAVE_MODAL_BUTTON)

    def click_filter_save_modal_button(self):
        self.click(self.locators.FILTER_SAVE_MODAL_BUTTON)

    def get_filter_form_error(self) -> str:
        return self.find(self.locators.FILTER_FORM_ERROR).text

    def enter_filter_title_modal_input(self, title: str):
        input = self.find(self.locators.FILTER_TITLE_MODAL_INPUT)
        input.clear()
        input.send_keys(title)
        
    def is_visible_filter_button(self) -> bool:
        return self.became_visible(self.locators.FILTER_BUTTON)

    def click_filter_button(self):
        self.click(self.locators.FILTER_BUTTON)

    def is_visible_saved_filter_button(self) -> bool:
        return self.became_visible(self.locators.SAVED_FILTER_BUTTON)

    def click_saved_filter_button(self):
        self.click(self.locators.SAVED_FILTER_BUTTON)

    def search_saved_filter(self, filter: str) -> bool:
        return self.became_visible(self.locators.SEARCH_SAVED_FILTER(filter))

    def delete_saved_filter(self, filter: str):
        self.click(self.locators.DELETE_SAVED_FILTER(filter))
        