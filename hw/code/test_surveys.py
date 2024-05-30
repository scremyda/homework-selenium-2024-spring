import pytest

from base import BaseCase


class TestSurveys(BaseCase):
    
    def test_skip_survey_description(self, serveys_page):
        serveys_page.open_lead_form_page()
        serveys_page.open_surveys_page()

        assert serveys_page.is_visible_create_survey()
        serveys_page.create_survey()
        assert serveys_page.get_header_new_survey()
        assert serveys_page.get_name_survey_input()
        assert serveys_page.get_company_name_survey_input()
        assert serveys_page.get_header_survey_input()
        assert serveys_page.get_description_survey_input()
        assert serveys_page.get_upload_survey_input()

        serveys_page.open_survey_questions()
        assert serveys_page.get_empty_field_alert()

    def test_choose_dark_theme_survey(self, serveys_page):
        serveys_page.open_lead_form_page()
        serveys_page.open_surveys_page()

        assert serveys_page.is_visible_create_survey()
        serveys_page.create_survey()

        assert serveys_page.get_dark_theme_survey()


    def test_choose_white_theme_survey(self, serveys_page):
        serveys_page.open_lead_form_page()
        serveys_page.open_surveys_page()

        assert serveys_page.is_enabled_create_survey()
        serveys_page.create_survey()

        assert serveys_page.get_white_theme_survey()


    def test_choose_question_survey(self, serveys_page):
        serveys_page.open_lead_form_page()
        serveys_page.open_surveys_page()

        assert serveys_page.is_enabled_create_survey()
        serveys_page.create_survey()

        assert serveys_page.get_name_survey_input()
        assert serveys_page.get_company_name_survey_input()
        assert serveys_page.get_header_survey_input()
        assert serveys_page.get_description_survey_input()
        assert serveys_page.get_upload_survey_input()

        serveys_page.write_name_survey_input(serveys_page.get_name_survey_input())

        serveys_page.write_company_name_survey_input(serveys_page.get_company_name_survey_input())

        serveys_page.write_header_survey_input(serveys_page.get_header_survey_input())

        serveys_page.write_description_survey_input(serveys_page.get_description_survey_input())

        serveys_page.open_upload_image()

        serveys_page.choose_upload_image()

        serveys_page.choose_questions()

        assert serveys_page.get_add_question()

        assert serveys_page.get_emergency_brake()

    def test_surveys_redirect(self, serveys_page):
        serveys_page.open_lead_form_page()

        serveys_page.open_surveys_page()
        assert serveys_page.get_create_survey()
        assert serveys_page.get_table_survey_name()
        assert serveys_page.get_table_survey_status()
        assert serveys_page.get_table_survey_list()
        assert serveys_page.get_table_survey_number()
        assert serveys_page.get_table_survey_date()
        assert serveys_page.get_table_survey_id()

    def test_create_survey_open(self, serveys_page):
        serveys_page.open_lead_form_page()

        serveys_page.open_surveys_page()
        assert serveys_page.get_create_survey()
        assert serveys_page.get_table_survey_name()
        assert serveys_page.get_table_survey_status()
        assert serveys_page.get_table_survey_list()
        assert serveys_page.get_table_survey_number()
        assert serveys_page.get_table_survey_date()
        assert serveys_page.get_table_survey_id()

        assert serveys_page.is_visible_create_survey()
        serveys_page.create_survey()
        assert serveys_page.get_header_new_survey()
        assert serveys_page.get_name_survey_input()
        assert serveys_page.get_company_name_survey_input()
        assert serveys_page.get_header_survey_input()
        assert serveys_page.get_description_survey_input()
        assert serveys_page.get_upload_survey_input()
        