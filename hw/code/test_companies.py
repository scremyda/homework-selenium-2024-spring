import pytest

from ui.pages.companies_page import CompaniesPage
from base import BaseCase


class TestCompanies(BaseCase):
    
    def test_campaigns_search_min_length(self, companies_page):

        assert companies_page.is_visible_enter_search_query()
        companies_page.enter_search_query("no")
        assert companies_page.is_visible_warning_min_length()
    
    def test_campaigns_search_save_button(self, companies_page):
        
        assert companies_page.is_visible_enter_search_query()
        companies_page.enter_search_query("query")
        assert companies_page.is_visible_filter_save_button()
    
    def test_campaigns_search_save_filter_error(self, companies_page):

        assert companies_page.is_visible_enter_search_query()
        companies_page.enter_search_query("query")
        assert companies_page.is_visible_filter_save_button()
        companies_page.click_filter_save_button()
        assert companies_page.is_visible_filter_save_modal_button()
        companies_page.click_filter_save_modal_button()
        assert companies_page.get_filter_form_error() == "Введите название фильтра"
    
    def test_campaigns_search_save_filter(self, companies_page):
        
        assert companies_page.is_visible_enter_search_query()
        companies_page.enter_search_query("query")
        assert companies_page.is_visible_filter_save_button()
        companies_page.click_filter_save_button()
        assert companies_page.is_visible_filter_save_modal_button()
        title = "filter1"
        companies_page.enter_filter_title_modal_input("filter1")
        companies_page.click_filter_save_modal_button()
        assert companies_page.is_visible_filter_button()
        companies_page.click_filter_button()
        assert companies_page.is_visible_saved_filter_button
        companies_page.click_saved_filter_button()
        assert companies_page.search_saved_filter(title)
        companies_page.delete_saved_filter(title)
    
    def test_campaigns_search_nonexistent(self, companies_page):
        
        assert companies_page.is_visible_enter_search_query()
        companies_page.enter_search_query("nonexistent_company")
        assert companies_page.is_visible_no_result()

    def test_campaign_creation_website_section(self, companies_page):
        
        assert companies_page.is_visible_create_company_btn()
        companies_page.click_create_company_btn()
        assert companies_page.is_visible_site_target()
        companies_page.select_site_target()
        assert companies_page.is_visible_target_site_input()

    def test_campaign_creation_website_section_error(self, companies_page):
        
        assert companies_page.is_visible_create_company_btn()
        companies_page.click_create_company_btn()
        assert companies_page.is_visible_site_target()
        companies_page.select_site_target()
        companies_page.click_contitnue_btn()
        assert companies_page.get_alert() == companies_page.NEED_FIELD_ALERT

    def test_campaign_creation_website_section_budget_error(self, companies_page):

        assert companies_page.is_visible_create_company_btn()
        companies_page.click_create_company_btn()
        assert companies_page.is_visible_site_target()
        companies_page.select_site_target()
        assert companies_page.is_visible_input_site()
        companies_page.input_site_value(companies_page.TARGET_SITE)
        companies_page.click_contitnue_btn()
        assert companies_page.get_alert() == companies_page.NEED_FIELD_ALERT

    def test_campaign_creation_website_section_budget_low_error(self, companies_page):
        
        assert companies_page.is_visible_create_company_btn()
        companies_page.click_create_company_btn()
        assert companies_page.is_visible_site_target()
        companies_page.select_site_target()
        assert companies_page.is_visible_input_site()
        companies_page.input_site_value(CompaniesPage.TARGET_SITE)
        assert companies_page.is_visible_input_budget()
        companies_page.input_budget_value(CompaniesPage.LOW_BUDGET)
        companies_page.click_contitnue_btn()
        assert companies_page.get_alert() == companies_page.LOW_BUDGET_ALERT

    def test_campaign_creation_website_section_next_step(self, companies_page):
        
        assert companies_page.is_visible_create_company_btn()
        companies_page.click_create_company_btn()
        assert companies_page.is_visible_site_target()
        companies_page.select_site_target()
        assert companies_page.is_visible_input_site()
        companies_page.input_site_value(CompaniesPage.TARGET_SITE)
        assert companies_page.is_visible_input_budget()
        companies_page.input_budget_value(CompaniesPage.HIGH_BUDGET)
        companies_page.click_contitnue_btn()
        assert companies_page.is_visible_second_step()

    def test_campaign_creation_mobile_app_section(self, companies_page):

        assert companies_page.is_visible_create_company_btn()
        companies_page.click_create_company_btn()
        assert companies_page.is_visible_mobileapp_target()
        companies_page.select_mobileapp_target()
        assert companies_page.is_visible_mobile_target_input()

    def test_drafts_search_ability(self, companies_page):

        assert companies_page.is_visible_create_company_btn()
        companies_page.click_create_company_btn()
        assert companies_page.is_visible_site_target()
        companies_page.select_site_target()
        assert companies_page.is_visible_input_site()
        companies_page.input_site_value(CompaniesPage.TARGET_SITE)
        assert companies_page.is_visible_input_budget()
        companies_page.input_budget_value(CompaniesPage.HIGH_BUDGET)
        companies_page.click_contitnue_btn()

        assert companies_page.is_visible_second_step()
        companies_page.click_save_draft_btn()
        companies_page.is_visible_save_draft_status()
        company_id = companies_page.driver.current_url.split('/')[-3]
        companies_page.go_to_root()

        companies_page.scroll_and_click_companies_menu_btn()
        assert companies_page.is_visible_drafts_btn()
        companies_page.click_drafts_btn()
        assert companies_page.is_visible_enter_search_query()
        companies_page.enter_search_query(company_id)
        assert not companies_page.is_visible_no_result()

    def test_drafts_search_empty(self, companies_page):
        
        assert companies_page.is_visible_create_company_btn()
        companies_page.click_create_company_btn()
        assert companies_page.is_visible_site_target()
        companies_page.select_site_target()
        assert companies_page.is_visible_input_site()
        companies_page.input_site_value(CompaniesPage.TARGET_SITE)
        assert companies_page.is_visible_input_budget()
        companies_page.input_budget_value(CompaniesPage.HIGH_BUDGET)
        companies_page.click_contitnue_btn()

        assert companies_page.is_visible_second_step()
        companies_page.click_save_draft_btn()
        companies_page.is_visible_save_draft_status()
        company_id = companies_page.driver.current_url.split('/')[-3]
        companies_page.go_to_root()

        companies_page.scroll_and_click_companies_menu_btn()
        assert companies_page.is_visible_drafts_btn()
        companies_page.click_drafts_btn()
        assert companies_page.is_visible_enter_search_query()
        companies_page.enter_search_query('nonexistent_company')
        assert companies_page.is_visible_no_result()
