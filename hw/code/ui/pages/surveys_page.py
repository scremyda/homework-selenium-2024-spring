from ui.locators.surveys_locators import SurveysPageLocators
from ui.pages.base_page import BasePage

class SurveysPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = SurveysPageLocators()

    def open_surveys_page(self):
        self.click(self.locators.OPEN_SURVEYS)

    def open_lead_form_page(self):
        self.click(self.locators.OPEN_LEAD_FORMS)

