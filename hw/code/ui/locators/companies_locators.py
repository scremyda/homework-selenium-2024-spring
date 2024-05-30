from selenium.webdriver.common.by import By


class CompaniesPageLocators:

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
        "//div[@data-id='mobapps']"
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

    WARNING_MIN_LENGTH = (
        By.XPATH,
        "//div[text()='Минимальное количество символов 3']"
    )

    FILTER_SAVE_BUTTON = (
        By.XPATH,
        "//span[text()='Сохранить']"
    )

    FILTER_SAVE_MODAL_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'SaveFilterModal_button')]/descendant::span[text()='Сохранить']"
    )

    FILTER_FORM_ERROR = (
        By.XPATH,
        "//span[@role='alert']/div"
    )

    FILTER_TITLE_MODAL_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'vkuiInput__el')]"
    )

    FILTER_BUTTON = (
        By.XPATH,
        "//span[text()='Фильтр']"
    )

    SAVED_FILTER_BUTTON = (
        By.XPATH,
        "//span[text()='Сохранённые']"
    )

    @staticmethod
    def SEARCH_SAVED_FILTER(filter):
        return By.XPATH, f"//span[contains(@class, 'vkuiTypography ') and text()='{filter}']"

    @staticmethod
    def DELETE_SAVED_FILTER(filter):
        return By.XPATH, f"//span[contains(@class, 'vkuiTypography ') and text()='{filter}']/following-sibling::span[@class='vkuiSimpleCell__badge']"