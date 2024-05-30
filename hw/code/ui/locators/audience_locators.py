from selenium.webdriver.common.by import By


class AudiencePageLocators:

    EMPTY_MESSAGE = (
        By.XPATH,
        "//h2[text()='Аудиторий пока нет']"
    )

    AUDIENCE_SEARCH_FIELD = (
        By.XPATH,
        "//input[@data-testid='search-input']"
    )

    ZERO_SEARCH_RESULT = (
        By.XPATH,
        "//h2[text()='Ничего не нашлось']"
    )

    CREATE_AUDIENCE_BUTTON = (
        By.XPATH,
        "//button[@data-testid='create-audience']"
    )

    TITLE_INPUT = (
        By.XPATH, 
        "//input[contains(@class, 'vkuiInput__el')]"
    )

    FORM_ERROR = (
        By.XPATH,
        "//span[@role='alert']"
    )

    USER_LIST_TAB = (
        By.XPATH,
        "//span[text()='Списки пользователей']"
    )

    CREATE_USER_LIST_BUTTON = (
        By.XPATH,
        "//button[@data-testid='create-audience']"
    )

    USER_LIST_TYPE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'vkuiCustomSelectInput__el')]"
    )

    USER_LIST_TYPE_SELECT = (
        By.XPATH,
        "//select[@class='vkuiCustomSelect__control']"
    )

    USER_LIST_FILE_INPUT = (
        By.CSS_SELECTOR, 
        "input[type='file']"
    )

    LOAD_FILE = (
        By.XPATH,
        "//div[contains(@class, 'LocalFileSelector')]"
    )

    USER_LIST_SAVE_BUTTON = (
        By.XPATH,
        "//span[text()='Сохранить']"
    )

    MODAL_ERROR_SAVE_FILE = (
        By.XPATH,
        "//h2[text()='Не удалось загрузить файл']"
    )
    
    USER_LIST_SEARCH_FIELD = (
        By.XPATH,
        "//input[@data-testid='search-input']"
    )

    TITLE_LENGTH = (
        By.XPATH,
        "//div[contains(@class, 'CreateSegmentModal')]/child::div[@class='']"
    )

    SELECTOR_CONDITIONAL_BUTTON = (
        By.XPATH,
        "//h4[text()='Включить пользователей, которые соответствуют']/descendant::div[contains(@class, 'HintSelector')]"
    )

    @staticmethod
    def SELECT_CONDITION(condition):
        return By.XPATH, f"//span[text()='{condition}']"

    CLOSE_ICON = (
        By.XPATH,
        "//button[@aria-label='Close']"
    )

    WARNING_MODEL = (
        By.XPATH,
        "//h2[text()='Прервать создание?']"
    )