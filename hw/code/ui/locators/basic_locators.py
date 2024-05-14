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
    EXPECTED_COMMON_URL = "https://ads.vk.com/hq/settings"
    EXPECTED_COMMON_ABOUT_ACCESS_URL = "https://ads.vk.com/help/articles/help_api"

    INPUT_ADD_ACCOUNT_VK_ID = "test123456789"
    INPUT_ATTRIBUTE = "value"

    OPEN_SETTINGS = (
        By.XPATH, "//*[contains(@class, 'vkuiSimpleCell__content') and text()='Настройки']"
    )

    OPEN_ACCESS_RIGHTS = (
        By.XPATH, "//*[contains(@class, 'vkuiTabsItem__label') and text()='Права доступа']"
    )

    OPEN_COMMON = (
        By.XPATH, "//*[contains(@class, 'vkuiTabsItem__label') and text()='Общие']"
    )

    OPEN_ACCESS_RIGHTS_DETAILS = (
        By.XPATH, "//*[contains(@class, 'vkuiInternalTappable') and text()='Подробнее']"
    )

    OPEN_ACCESS_RIGHTS_ADD_ACCOUNT = (
        By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить кабинет']"
    )

    CLOSE_ACCESS_RIGHTS_ADD_ACCOUNT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiModalDismissButton')]"
    )

    WINDOW_ACCESS_RIGHTS_ADD_ACCOUNT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTypography') and text()='Добавление кабинета']"
    )

    WINDOW_ACCESS_RIGHTS_ADD_ACCOUNT_ID = (
        By.XPATH,
        "//*[contains(@class, 'vkuiInput__el')]"
    )

    WINDOW_ACCESS_RIGHTS_ADD_ACCOUNT_ID_SAVE = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__content') and text()='Сохранить']"
    )

    WINDOW_ACCESS_RIGHTS_ADD_ACCOUNT_ID_ERROR = (
        By.XPATH,
        "//*[@role='alert' and text()='Обязательное поле']"
    )

    OPEN_USER_LANGUAGE_LIST = (
        By.XPATH, "//*[@role='combobox' and @aria-expanded='false']"
    )

    USER_LANGUAGE_LIST = (
        By.XPATH,
        "//*[contains(@class, 'vkuiCustomSelectInput__title') and text()='RU']"
    )

    OPEN_MORE_ABOUT_ACCESS = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTappable') and text()='Подробнее о доступе']"
    )
