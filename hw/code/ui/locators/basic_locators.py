from selenium.webdriver.common.by import By


class BasePageLocators:

    @staticmethod
    def BY_MAIL_TEST_ID(id):
        return (By.XPATH, f"//*[@data-test-id='{id}']")
