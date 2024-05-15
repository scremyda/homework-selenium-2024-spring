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

    EXPECTED_NOTIFICATIONS_URL = "https://ads.vk.com/hq/settings/notifications"
    EXPECTED_NOTIFICATIONS_CONNECT_TG_URL = "https://t.me/vkadssenderbot"

    EXPECTED_CHANGED_HISTORY_URL = "https://ads.vk.com/hq/settings/logs"

    INPUT_ADD_ACCOUNT_VK_ID = "test123456789"
    INPUT_ATTRIBUTE = "value"

    OPEN_SETTINGS = (
        By.XPATH, "//*[contains(@class, 'vkuiSimpleCell__content') and text()='Настройки']"
    )

    OPEN_ACCESS_RIGHTS = (
        By.XPATH, "//*[contains(@class, 'vkuiTabsItem__label') and text()='Права доступа']"
    )

    OPEN_HISTORY_OF_CHANGES = (
        By.XPATH, "//*[contains(@class, 'vkuiTabsItem__label') and text()='История изменений']"
    )

    OPEN_HISTORY_OF_CHANGES_FILTER = (
        By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Фильтр']"
    )

    OPEN_COMMON = (
        By.XPATH, "//*[contains(@class, 'vkuiTabsItem__label') and text()='Общие']"
    )

    OPEN_NOTIFICATIONS = (
        By.XPATH, "//*[contains(@class, 'vkuiTabsItem__label') and text()='Уведомления']"
    )

    OPEN_CONNECT_TG = (
        By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Подключить']"
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
        "//*[contains(@class, 'vkuiModalPage') ]"
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

    HISTORY_FILTER = (
        By.XPATH,
        "//*[contains(@class, 'FilterBlock_layout__UVMxX')]"
    )

    OPEN_MORE_ABOUT_ACCESS = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTappable') and text()='Подробнее о доступе']"
    )

class CompaniesPageLocators(BasePageLocators):

    SKIP_HELP_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__content') and text()='Попробовать позже']"
    )

    CREATE_BUTTON = (
        By.XPATH,
         '//*[@data-testid="create-button"]'
    )

    PLANS_BUTTON = (
        By.XPATH,
         "//*[starts-with(@id, 'dashboard') and contains(@id, '.plans')]"
    )

    GROUPS_BUTTON = (
        By.XPATH, 
        "//*[starts-with(@id, 'dashboard') and contains(@id, '.groups')]"
    )

    ADS_BUTTON = (
        By.XPATH, 
        "//*[starts-with(@id, 'dashboard') and contains(@id, '.ads')]"
    )

    SITE_TARGET = (
        By.XPATH,
        "//*[@data-id='site_conversions']"
    )

    SITE_INPUT = (
        By.XPATH,
        "//*[@placeholder='Введите ссылку на сайт']"
    )

    BUDGET_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'Budget_input__')]/input"
    )

    CONTINUE_BUTTON = (
        By.XPATH,
        "//*[@id='footer']//button"
    )
    
    MOBILEAPP_TARGET = (
        By.XPATH,
        "//*[@data-id='mobapps']"
    )

    TARGET_INPUT = (
        By.XPATH,
        '//*[@id="new_ad_create"]/div/div/div/div/div/section[3]/form/div/div/div[1]'
    )

    MOBILE_TARGET_INPUT = (
        By.XPATH,
        "//*[@placeholder='Выберите приложение']"
    )

    ROOT = (
        By.CLASS_NAME, 
        'header_logo__7lhb6'
    )

    DROPDOWN_BUTTON = (
        By.XPATH, 
        "//*[@id='adPlan']/div/div[2]/div/div[1]/div/div[1]/div"
    )

    DRAFTS_BUTTON = (By.XPATH, '//*[@data-testid="drafts-button"]')

    SEARCH_FIELD = (By.XPATH, '//*[@data-testid="filter-search-input"]')
