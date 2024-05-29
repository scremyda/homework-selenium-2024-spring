from ui.pages.companies_page import CompaniesPage

from base import BaseCase


class TestCompanies(BaseCase):

    def test_redirect_create_page(self, companies_page):
        companies_page.skip_help()
        companies_page.click_create_btn()

        assert self.is_url_open('https://ads.vk.com/hq/new_create/ad_plan')

    def test_redirect_groups_table(self, companies_page):
        companies_page.skip_help()
        companies_page.click_groups_btn()

        assert self.is_url_open('https://ads.vk.com/hq/dashboard/ad_groups')

    def test_redirect_ads_table(self, companies_page):
        companies_page.skip_help()
        companies_page.click_ads_btn()

        assert self.is_url_open('https://ads.vk.com/hq/dashboard/ads')

    def test_redirect_plans_table(self, companies_page):
        companies_page.skip_help()    
        companies_page.click_ads_btn()
        companies_page.click_plans_btn()

        assert self.is_url_open('https://ads.vk.com/hq/dashboard/ad_plans')

    def test_form_site_is_open(self, companies_page):
        companies_page.skip_help()
        companies_page.click_create_btn()
        companies_page.wait_site_target()
        companies_page.select_site_target()

        assert companies_page.became_visible_target_input()

    def test_site_target_site_is_need(self, companies_page):
        companies_page.skip_help()
        companies_page.click_create_btn()
        companies_page.wait_site_target()
        companies_page.select_site_target()
        companies_page.click_contitnue_btn()

        assert companies_page.get_alert() == companies_page.NEED_FIELD_ALERT 

    def test_budget_value_is_need(self, companies_page):
        companies_page.skip_help()
        companies_page.click_create_btn()
        companies_page.wait_site_target()
        companies_page.select_site_target()
        companies_page.wait_input_site()
        companies_page.input_site_value(companies_page.TARGET_SITE)
        companies_page.click_contitnue_btn()

        assert ompanies_page.get_alert() == companies_page.NEED_FIELD_ALERT
        
    def test_low_budget(self, companies_page):
        companies_page.skip_help()
        companies_page.click_create_btn()
        companies_page.wait_site_target()
        companies_page.select_site_target()
        companies_page.wait_input_site()
        companies_page.input_site_value(CompaniesPage.TARGET_SITE)
        companies_page.wait_input_budget()
        companies_page.input_budget_value(CompaniesPage.LOW_BUDGET)
        companies_page.click_contitnue_btn()

        assert companies_page.get_alert() == companies_page.LOW_BUDGET_ALERT

    def test_correct_data_saved(self, companies_page):
        companies_page.skip_help()
        companies_page.click_create_btn()
        companies_page.wait_site_target()
        companies_page.select_site_target()
        companies_page.wait_input_site()
        companies_page.input_site_value(CompaniesPage.TARGET_SITE)
        companies_page.wait_input_budget()
        companies_page.input_budget_value(CompaniesPage.CORRECT_BUDGET)
        companies_page.click_contitnue_btn()

        assert companies_page.became_visible_second_step()

    def test_form_mobile_is_open(self, companies_page):
        companies_page.skip_help()
        companies_page.click_create_btn()
        companies_page.select_mobileapp_target()

        assert companies_page.became_visible_mobile_target_input()

    def test_drafts_search_ability(self, companies_page):
        companies_page.skip_help()
        companies_page.click_create_btn()
        companies_page.wait_site_target()
        companies_page.select_site_target()
        companies_page.wait_input_site()
        companies_page.input_site_value(CompaniesPage.TARGET_SITE)
        companies_page.wait_input_budget()
        companies_page.input_budget_value(CompaniesPage.CORRECT_BUDGET)
        companies_page.click_contitnue_btn()

        companies_page.click_save_draft_btn()
        companies_page.became_visible_save_draft_status()
        company_id = companies_page.driver.current_url.split('/')[-3]
        companies_page.go_to_root()

        companies_page.click_companies_menu_btn()
        companies_page.click_drafts_btn()
        companies_page.input_search_query(company_id)

        assert not companies_page.became_visible_no_result()

    def test_drafts_search_empty(self, companies_page):
        companies_page.skip_help()
        companies_page.click_create_btn()
        companies_page.wait_site_target()
        companies_page.select_site_target()
        companies_page.wait_input_site()
        companies_page.input_site_value(CompaniesPage.TARGET_SITE)
        companies_page.wait_input_budget()
        companies_page.input_budget_value(CompaniesPage.CORRECT_BUDGET)
        companies_page.click_contitnue_btn()

        companies_page.click_save_draft_btn()
        companies_page.became_visible_save_draft_status()
        company_id = companies_page.driver.current_url.split('/')[-1]
        companies_page.go_to_root()

        companies_page.click_companies_menu_btn()
        companies_page.click_drafts_btn()
        companies_page.input_search_query('Не существующая компания')

        assert companies_page.became_visible_no_result()
