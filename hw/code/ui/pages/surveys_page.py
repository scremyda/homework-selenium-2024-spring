import time

from ui.locators.surveys_locators import SurveysPageLocators
from ui.pages.base_page import BasePage

class SurveysPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = SurveysPageLocators()

    def open_surveys_page(self):
        self.click(self.locators.OPEN_SURVEYS)

    def create_survey(self):
        self.click(self.locators.CREATE_SURVEY, 5)

    def is_visible_create_survey(self) -> bool:
        return self.became_visible(self.locators.CREATE_SURVEY)
    
    def is_enabled_create_survey(self) -> bool:
        return self.is_enabled(self.locators.CREATE_SURVEY)

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
        return self.find(self.locators.FORM_DARK_THEME_SURVEY)

    def get_white_theme_survey(self):
        return self.find(self.locators.FORM_WHITE_THEME_SURVEY)

    def write_name_survey_input(self, input_vk_id):
        input_vk_id.send_keys(self.locators.INPUT_TEST_LOGIC)

    def write_company_name_survey_input(self, input_vk_id):
        input_vk_id.send_keys(self.locators.INPUT_TEST_LOGIC)

    def write_header_survey_input(self, input_vk_id):
        input_vk_id.send_keys(self.locators.INPUT_TEST_LOGIC)

    def write_description_survey_input(self, input_vk_id):
        input_vk_id.send_keys(self.locators.INPUT_TEST_LOGIC)

    def open_upload_image(self):
        self.click(self.locators.SURVEY_UPLOAD_INPUT)

    def choose_upload_image(self):
        self.click(self.locators.CHOOSE_DEFAULT_IMAGE)

    def choose_questions(self):
        time.sleep(2)
        self.click(self.locators.CHOOSE_QUESTIONS,5)

    def get_emergency_brake(self):
        return self.find(self.locators.CHOOSE_EMERGENCY_BREAK)

    def get_add_question(self):
        return self.find(self.locators.CHOOSE_ADD_QUESTIONS)

    def get_questions(self):
        return self.find(self.locators.CHOOSE_QUESTIONS)

