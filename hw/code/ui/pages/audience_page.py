from selenium.common.exceptions import TimeoutException

from ui.locators.audience_locators import AudiencePageLocators
from ui.pages.base_page import BasePage

class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators()

    def test_check_access_redirect(self):
        print("unimplemented")