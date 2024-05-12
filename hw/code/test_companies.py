from base import BaseCase
from ui.pages.companies_page import CompaniesPage

class TestCompanies(BaseCase):

    #Кампании. Выполняется переход на https://ads.vk.com/hq/new_create/ad_plan после клика по кнопке Создать
    def test_redirect_create_page(self, companies_page):
            companies_page.click_create_btn()

            time.sleep(2)
            assert self.is_url_open('https://ads.vk.com/hq/new_create/ad_plan')