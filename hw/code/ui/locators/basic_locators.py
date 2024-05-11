from selenium.webdriver.common.by import By


class BasePageLocators:

    @staticmethod
    def BY_MAIL_TEST_ID(id):
        return (By.XPATH, f"//*[@data-test-id='{id}']")





class RegistrationMainPageLocators(BasePageLocators):
    MAIL_RU_AUTH = BasePageLocators.BY_MAIL_TEST_ID("oAuthService_mail_ru")
    MAIL_RU_SHOW_PASSWORD = BasePageLocators.BY_MAIL_TEST_ID("next-button")
    MAIL_RU_LOGIN = (By.NAME, "username")
    MAIL_RU_PASSWORD = (By.NAME, "password")
    MAIL_RU_SUBMIT = BasePageLocators.BY_MAIL_TEST_ID("submit-button")


class RegistrationPageLocators(BasePageLocators):
    EMAIL_INPUT = (By.NAME, "email")


class SettingsPageLocators(BasePageLocators):
    EXPECTED_ACCESS_URL = "https://ads.vk.com/hq/settings/access"

    OPEN_SETTINGS = (
        By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/div/div[1]/div/section[2]/a")

    OPEN_ACCESS_RIGHTS = (
        By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div/div/div[1]/div/div[3]")
