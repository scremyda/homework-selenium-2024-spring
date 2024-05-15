from base import BaseCase
from ui.pages.companies_page import CompaniesPage

class TestCompanies(BaseCase):

    def test_redirect_create_page(self, companies_page):
        companies_page.click_create_btn()

        time.sleep(2)
        assert self.is_url_open('https://ads.vk.com/hq/new_create/ad_plan')


    def test_redirect_groups_table(self, companies_page):
            companies_page.click_groups_btn()

            time.sleep(2)
            assert self.is_url_open('https://ads.vk.com/hq/dashboard/ad_groups')

    def test_redirect_plans_table(self, companies_page):
            companies_page.click_ads_btn()

            time.sleep(2)
            assert self.is_url_open('https://ads.vk.com/hq/dashboard/ads')

    def test_redirect_plans_table(self, companies_page):
        companies_page.click_ads_btn()

        companies_page.click_plans_btn()

        time.sleep(2)
        assert self.is_url_open('https://ads.vk.com/hq/dashboard/ad_plans')

    def test_form_site_is_open(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        assert(companies_page.get_target_input() is not None)
    

    def test_site_target_site_is_need(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        companies_page.click_contitnue_btn()
        assert ('Обязательное поле' in companies_page.driver.page_source)

    def test_budget_value_is_need(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        companies_page.input_site_value(self.TARGET_SITE)
        companies_page.click_contitnue_btn()
        assert ('Обязательное поле' in companies_page.driver.page_source)

    def test_low_budget(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        companies_page.input_site_value(self.TARGET_SITE)
        companies_page.input_budget_value(self.LOW_BUDGET)
        companies_page.click_contitnue_btn()
        assert (
            'Бюджет кампании должен быть не меньше 100₽' in companies_page.driver.page_source)

    def test_correct_data_saved (self, companies_page):
        companies_page.create_company(self.TARGET_SITE, self.CORRECT_BUDGET)
        assert ('ad_group' in companies_page.driver.current_url.split('/'))

    def test_form_mobile_is_open(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_mobileapp_target()
        assert(companies_page.get_mobile_target_input() is not None)

    def test_unfinished_company_to_drafts(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        companies_page.input_site_value(self.TARGET_SITE)
        company_id = companies_page.driver.current_url.split('/')[-1]
        companies_page.go_to_root()
        companies_page.click_drafts_btn()
        assert (company_id in companies_page.driver.page_source)

    def test_drafts_search_ability(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        companies_page.input_site_value(self.TARGET_SITE)
        company_id = companies_page.driver.current_url.split('/')[-1]
        companies_page.go_to_root()
        companies_page.click_drafts_btn()
        companies_page.input_search_query('Кампания')
        assert (company_id in companies_page.driver.page_source)

    def test_drafts_search_empty(self, companies_page):
        companies_page.click_create_btn()
        companies_page.select_site_target()
        companies_page.input_site_value(self.TARGET_SITE)
        company_id = companies_page.driver.current_url.split('/')[-1]
        companies_page.go_to_root()
        companies_page.click_drafts_btn()
        companies_page.input_search_query('Strange Name')
        assert (company_id not in companies_page.driver.page_source)