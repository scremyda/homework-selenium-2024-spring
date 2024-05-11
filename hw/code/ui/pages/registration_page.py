from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class RegistrationMainPage(BasePage):
    url = 'https://ads.vk.com/hq/registration'
    locators = basic_locators.RegistrationMainPageLocators()


    def login(self, login, password):
        self.click(self.locators.MAIL_RU_AUTH)
        self.fill_in(self.locators.MAIL_RU_LOGIN, login)
        self.click(self.locators.MAIL_RU_SHOW_PASSWORD)
        self.fill_in(self.locators.MAIL_RU_PASSWORD, password)
        self.click(self.locators.MAIL_RU_SUBMIT)


class RegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration/new'
    locators = basic_locators.RegistrationPageLocators()
