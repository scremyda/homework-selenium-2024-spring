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

    HEADER_ACCOUNTS = (
        By.XPATH, "//*[contains(@class, 'Summary_title') and text()='Мультиаккаунты']"
    )

    HEADER_ACCESS = (
        By.XPATH, "//*[contains(@class, 'Headline_title') and text()='Как дать доступ к своему кабинету']"
    )

    HEADER_CHANGE_ACCESS = (
        By.XPATH,
        "//*[contains(@class, 'Headline_title') and text()='Как изменить или отозвать доступ к своему кабинету']"
    )

    HEADER_OTHER_ACCOUNTS_ACCESS = (
        By.XPATH,
        "//*[contains(@class, 'Headline_title') and text()='Доступ к другим кабинетам']"
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

    OPEN_EXTENDED_RIGHTS = (
        By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Расширенные права']"
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

    TEXT_ACCESS_ACCOUNTS = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTypography') and text()='Доступа к другим кабинетам пока нет']"
    )

    BUTTON_ADD_ACCOUNTS = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton') and text()='Добавить кабинет']"
    )

    LINK_DETAILS= (
        By.XPATH,
        "//*[contains(@class, 'vkuiLink') and text()='Подробнее']"
    )

    ACCESS_COMPANIES = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTypography') and text()='Доступ к кампаниям']"
    )

    ACCESS_MONEY = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTypography') and text()='Доступ к финансовой информации']"
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
        "//*[contains(@class, 'FilterBlock_layout')]"
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

    SKIP_HELP_STEP = (
        By.XPATH,
        "//*[contains(@class, 'CloseButton_iconWrapper')]"
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
        "//input[@placeholder='Введите ссылку на сайт']"
    )

    BUDGET_INPUT = (
        By.XPATH,
        "//span[contains(@class, 'Budget_input')]/child::input"
    )

    CONTINUE_BUTTON = (
        By.XPATH,
        "//*[@id='footer']//button[contains(@class, 'primary')]"
    )
    
    MOBILEAPP_TARGET = (
        By.XPATH,
        "//*[@data-id='mobapps']"
    )

    MOBILE_TARGET_INPUT = (
        By.XPATH,
        "//*[@placeholder='Выберите приложение']"
    )

    SAVE_DRAFT_BUTTON = (
        By.XPATH,
        "//*[@class='vkuiButton__content' and text()='Сохранить как черновик']"
    )

    COMPANIES_MENU_BUTTON = (
        By.XPATH,
        "//span[text()='Кампании']/parent::div[contains(@class, 'MenuCell_text')]"
    )

    ROOT = (
        By.XPATH, 
        "//button[contains(@class, 'header_logo')]"
    )

    DRAFTS_BUTTON = (
        By.XPATH,
        "//button[@data-testid='drafts-button']"
    )

    SEARCH_FIELD = (
        By.XPATH,
        "//input[@data-testid='filter-search-input']"
    )

    NO_RESULT = (
        By.XPATH,
        "//span[contains(@class, 'EmptyPlaceholder_title')]"
    )

    ALERT = (
        By.XPATH,
        "//*[@role='alert']/div"
    )

    SAVE_DRAFT_STATUS = (
        By.XPATH,
        "//*[contains(@class, 'CreateFooter_draftStatus') and text()='Изменения сохранены']"
    )