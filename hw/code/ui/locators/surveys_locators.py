from selenium.webdriver.common.by import By


class SurveysPageLocators:
    INPUT_TEST_LOGIC = "test123456789"

    OPEN_SURVEYS = (
        By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Опросы']"
    )

    CREATE_SURVEY = (
        By.XPATH, "//span[text()='Создать опрос' and contains(@class, 'vkuiButton__content')]"
    )

    CREATE_SURVEYS_QUESTIONS = (
        By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Вопросы']"
    )

    NEW_SURVEY = (
        By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Новый опрос']"
    )

    OPEN_LEAD_FORMS = (
        By.XPATH, "//*[text()='Лид-формы и опросы']"
    )

    TABLE_SURVEY_NAME = (
        By.XPATH, "//*[contains(@class, 'BaseTable') and text()='Название опроса']"
    )

    TABLE_SURVEY_STATUS = (
        By.XPATH, "//*[contains(@class, 'BaseTable') and text()='Статус']"
    )

    TABLE_SURVEY_LIST = (
        By.XPATH, "//*[contains(@class, 'BaseTable') and text()='Список анкет']"
    )

    TABLE_SURVEY_NUMBER = (
        By.XPATH, "//*[contains(@class, 'BaseTable') and text()='Количество анкет']"
    )

    TABLE_SURVEY_DATE= (
        By.XPATH, "//*[contains(@class, 'BaseTable') and text()='Дата создания']"
    )

    FORM_WHITE_THEME_SURVEY = (
        By.XPATH, "//*[contains(@class, 'LeadForm-module')]"
    )

    CHOOSE_DEFAULT_IMAGE = (
        By.XPATH, "//*[contains(@class, 'ImageItems_image__')]"
    )

    TABLE_SURVEY_ID = (
        By.XPATH, "//*[contains(@class, 'BaseTable') and text()='ID']"
    )

    CHOOSE_QUESTIONS = (
        By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Вопросы']"
    )

    CHOOSE_EMERGENCY_BREAK = (
        By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить стоп-экран']"
    )

    CHOOSE_ADD_QUESTIONS = (
        By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить вопрос']"
    )


    GET_QUESTIONS = (
        By.XPATH, "//*[text()='Вопросы']"
    )

    SURVEY_NAME_INPUT = (
        By.XPATH, "//*[@placeholder='Введите название']"
    )

    SURVEY_COMPANY_NAME_INPUT = (
        By.XPATH, "//*[@placeholder='Введите название компании']"
    )

    SURVEY_HEADER_INPUT = (
        By.XPATH, "//*[@placeholder='Введите заголовок']"
    )

    SURVEY_DESCRIPTION_INPUT = (
        By.XPATH, "//*[@placeholder='Введите описание опроса']"
    )

    SURVEY_UPLOAD_INPUT = (
        By.XPATH, "//*[text()='Загрузить логотип']"
    )

    ALERT_EMPTY_FIELD = (
        By.XPATH, "//*[@role='alert']"
    )

    DARK_THEME_SURVEY = (
        By.XPATH, "//*[contains(@class, 'vkuiHeadline--level-2')]"
    )

    FORM_DARK_THEME_SURVEY = (
        By.XPATH, "//*[contains(@class, 'LeadForm-module')]"
    )
