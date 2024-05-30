from ui.locators.registration_locators import RegistrationPageLocators
from ui.pages.base_page import BasePage


class RegistrationMainPage(BasePage):
    url = 'https://ads.vk.com/hq/registration'
    locators = RegistrationPageLocators()

    def login(self, login, password):
        self.click(self.locators.MAIL_RU_AUTH)
        self.fill_in(self.locators.MAIL_RU_LOGIN, login)
        self.click(self.locators.MAIL_RU_SHOW_PASSWORD)
        self.fill_in(self.locators.MAIL_RU_PASSWORD, password)
        self.click(self.locators.MAIL_RU_SUBMIT)


class RegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration/new'
    locators = RegistrationPageLocators()
