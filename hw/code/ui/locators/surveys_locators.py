from selenium.webdriver.common.by import By


class SurveysPageLocators:
    OPEN_SURVEYS = (
        By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Опросы']"
    )

    CREATE_SURVEY = (
        By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Создать опрос']"
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

    TABLE_SURVEY_ID = (
        By.XPATH, "//*[contains(@class, 'BaseTable') and text()='ID']"
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
