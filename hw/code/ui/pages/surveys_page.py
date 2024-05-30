from ui.locators.surveys_locators import SurveysPageLocators
from ui.pages.base_page import BasePage

class SurveysPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = SurveysPageLocators()

    def open_surveys_page(self):
        self.click(self.locators.OPEN_SURVEYS)

    def create_survey(self):
        self.click(self.locators.CREATE_SURVEY)

    def open_survey_questions(self):
        self.click(self.locators.CREATE_SURVEYS_QUESTIONS)

    def get_header_new_survey(self):
        return self.find(self.locators.NEW_SURVEY)

    def get_create_survey(self):
        return self.find(self.locators.CREATE_SURVEY)

    def get_table_survey_name(self):
        return self.find(self.locators.TABLE_SURVEY_NAME)

    def get_table_survey_status(self):
        return self.find(self.locators.TABLE_SURVEY_STATUS)

    def get_table_survey_list(self):
        return self.find(self.locators.TABLE_SURVEY_LIST)

    def get_table_survey_number(self):
        return self.find(self.locators.TABLE_SURVEY_NUMBER)

    def get_table_survey_date(self):
        return self.find(self.locators.TABLE_SURVEY_DATE)

    def get_table_survey_id(self):
        return self.find(self.locators.TABLE_SURVEY_ID)

    def open_lead_form_page(self):
        self.click(self.locators.OPEN_LEAD_FORMS)

    def get_name_survey_input(self):
        return self.find(self.locators.SURVEY_NAME_INPUT)

    def get_company_name_survey_input(self):
        return self.find(self.locators.SURVEY_COMPANY_NAME_INPUT)

    def get_header_survey_input(self):
        return self.find(self.locators.SURVEY_HEADER_INPUT)

    def get_description_survey_input(self):
        return self.find(self.locators.SURVEY_DESCRIPTION_INPUT)

    def get_upload_survey_input(self):
        return self.find(self.locators.SURVEY_UPLOAD_INPUT)

    def get_empty_field_alert(self):
        return self.find(self.locators.ALERT_EMPTY_FIELD)

    def choose_dark_theme_survey(self):
        self.click(self.locators.DARK_THEME_SURVEY)

    def get_dark_theme_survey(self):
        element =  self.find(self.locators.FORM_DARK_THEME_SURVEY)
        bg_color = element.get_css_property("background-color")

        # Проверка, что цвет фона точно соответствует #141414
        if bg_color.strip() == "#141414":
            print("Цвет фона элемента точно соответствует #141414.")
        else:
            print("Цвет фона элемента не соответствует #141414. Текущий цвет:", bg_color)

