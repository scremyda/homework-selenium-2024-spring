from selenium.webdriver.common.by import By


class SurveysPageLocators:
    OPEN_SURVEYS = (
        By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Опросы']"
    )

    OPEN_LEAD_FORMS = (
        By.XPATH, "//*[text()='Лид-формы и опросы']"
    )