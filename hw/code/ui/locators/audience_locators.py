from selenium.webdriver.common.by import By


class AudiencePageLocators:

    SAVE_DRAFT_STATUS = (
        By.XPATH,
        "//*[contains(@class, 'CreateFooter_draftStatus') and text()='Изменения сохранены']"
    )