from selenium.webdriver.common.by import By


class SettingsPageLocators:
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
        By.XPATH, "//*[contains(@class, 'Telegram_title') and text()='Сообщение в Telegram']"
    )

    OPEN_ACCESS_RIGHTS_DETAILS = (
        By.XPATH, "//*[contains(@class, 'vkuiInternalTappable') and text()='Подробнее']"
    )

    OPEN_ACCESS_RIGHTS_ADD_ACCOUNT = (
        By.XPATH, "//*[contains(@class, 'vkuiButton') and text()='Добавить кабинет']"
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