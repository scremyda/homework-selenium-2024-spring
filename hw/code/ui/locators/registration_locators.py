from selenium.webdriver.common.by import By

from ui.locators.basic_locators import BasePageLocators

class RegistrationPageLocators(BasePageLocators):
    MAIL_RU_AUTH = BasePageLocators.BY_MAIL_TEST_ID("oAuthService_mail_ru")
    MAIL_RU_SHOW_PASSWORD = BasePageLocators.BY_MAIL_TEST_ID("next-button")
    MAIL_RU_LOGIN = (By.NAME, "username")
    MAIL_RU_PASSWORD = (By.NAME, "password")
    MAIL_RU_SUBMIT = BasePageLocators.BY_MAIL_TEST_ID("submit-button")
    EMAIL_INPUT = (By.NAME, "email")
