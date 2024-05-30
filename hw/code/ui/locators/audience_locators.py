from selenium.webdriver.common.by import By


class AudiencePageLocators:

    EMPTY_MASSAGE = (
        By.XPATH,
        "//h2[text()='Аудиторий пока нет']"
    )