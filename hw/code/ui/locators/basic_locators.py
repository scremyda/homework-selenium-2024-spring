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
    EXPECTED_ACCESS_DETAILS_URL = "https://ads.vk.com/help/articles/additionalaccounts"

    INPUT_ADD_ACCOUNT_VK_ID = "test123456789"
    INPUT_ATTRIBUTE = "value"

    OPEN_SETTINGS = (
        By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/div/div[1]/div/section[2]/a"
    )

    OPEN_ACCESS_RIGHTS = (
        By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div/div/div[1]/div/div[3]"
    )

    OPEN_ACCESS_RIGHTS_DETAILS = (
        By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div/div/div[2]/section/div/div/div/div/div/div[2]/div/h4/div/span/a"
    )

    OPEN_ACCESS_RIGHTS_ADD_ACCOUNT = (
        By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div/div/div[2]/section/div/div/div/div/div/div[2]/div/div[2]/button/span"
    )

    CLOSE_ACCESS_RIGHTS_ADD_ACCOUNT = (
        By.XPATH,
        "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[3]"
    )

    WINDOW_ACCESS_RIGHTS_ADD_ACCOUNT = (
        By.XPATH,
        "/html/body/div[1]/div/div[3]/div"
    )

    WINDOW_ACCESS_RIGHTS_ADD_ACCOUNT_ID = (
        By.XPATH,
        "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/div[1]/div/form/div[1]/div/div[1]/span/input"
    )
