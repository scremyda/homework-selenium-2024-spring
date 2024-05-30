import pytest, time

from ui.pages.audience_page import AudiencePage
from base import BaseCase


class TestAudience(BaseCase):

    @pytest.mark.skip
    def test_audience_empty_message_displayed(self, audience_page):

        assert audience_page.is_visible_empty_message()

    @pytest.mark.skip
    def test_nonexistent_audience_search_displays_nothing(self, audience_page):

        audience_page.enter_search_audience("nonexistent_audience")
        assert audience_page.is_visible_zero_search_result()
    
    @pytest.mark.skip
    def test_user_list_max_length_error(self, audience_page):

        audience_page.open_user_list_tab()
        audience_page.click_create_user_list_button()
        assert audience_page.is_visible_title_input()
        audience_page.clear_and_enter_user_list_title((audience_page.MAX_LENGTH_TITLE+1) * 'n')
        assert audience_page.is_visible_title_input_form_error() == "Превышена длина названия списка"
    
    @pytest.mark.skip
    def test_user_list_empty_title_error(self, audience_page):

        audience_page.open_user_list_tab()
        audience_page.click_create_user_list_button()
        assert audience_page.is_visible_title_input()
        audience_page.clear_and_enter_user_list_title('   ')
        assert audience_page.is_visible_title_input_form_error() == "Обязательное поле"

    @pytest.mark.skip
    def test_user_list_invalid_file_format_modal_displayed(self, audience_page):
        
        audience_page.open_user_list_tab()
        audience_page.click_create_user_list_button()
        assert audience_page.is_visible_user_list_type_input()
        audience_page.select_user_list_type_vk()
        audience_page.load_user_list_file("groups.xlsx")
        audience_page.click_user_list_save_button()
        assert is_visible_modale_save_file_error()

    @pytest.mark.skip 
    def test_vk_id_list_successfully_saved(self, audience_page):
        audience_page.open_user_list_tab()
        audience_page.click_create_user_list_button()
        assert audience_page.is_visible_user_list_type_input()
        assert audience_page.is_visible_title_input()
        title = audience_page.get_title_data()
        audience_page.select_user_list_type_vk()
        audience_page.load_user_list_file("success.txt")
        audience_page.click_user_list_save_button()
        assert is_visible_search_user_list_field()
        audience_page.enter_search_user_list(title)
        assert not audience_page.is_visible_zero_search_result()
    
    @pytest.mark.skip 
    def test_user_list_default_title_generation(self, audience_page):

        audience_page.open_user_list_tab()
        audience_page.click_create_user_list_button()
        assert audience_page.is_visible_title_input()
        title = audience_page.get_title_data()
        assert audience_page.check_user_list_title(title)

    @pytest.mark.skip 
    def test_audience_creation_modal_default_name(self, audience_page):
        
        assert audience_page.is_visible_create_audience_button()
        audience_page.click_create_audience_button()
        assert audience_page.is_visible_title_input()
        title = audience_page.get_title_data()
        assert audience_page.check_audience_title(title)

    @pytest.mark.skip 
    def test_audience_name_max_length_error(self, audience_page):
        
        assert audience_page.is_visible_create_audience_button()
        audience_page.click_create_audience_button()
        audience_page.enter_audience_title((audience_page.MAX_LENGTH_TITLE_NAME+1) * 'n')
        assert audience_page.get_form_error() == "Максимальная длина 255 символов"

    @pytest.mark.skip   
    def test_audience_name_character_count_displayed(self, audience_page):

        assert audience_page.is_visible_create_audience_button()
        audience_page.click_create_audience_button()
        count = 99
        audience_page.enter_audience_title(count * 'n')
        assert audience_page.get_title_length() == count

    def test_change_matching_condition_modal_displayed(self, audience_page):

        assert audience_page.is_visible_create_audience_button()
        audience_page.click_create_audience_button()
        assert audience_page.is_visible_selector_conditional_button()
        current_condition = audience_page.get_current_selector_conditional_button()
        next_condition = audience_page.calculate_next_condition(current_condition)
        audience_page.click_selector_conditional_button()
        audience_page.select_conditional(next_condition)
        audience_page.click_close_icon()
        assert audience_page.is_visible_warning_modal()
"""
    def test_vk_group_search_results_displayed(self, audience_page):
        pass

    def test_select_all_groups_button_activates_save_button(self, audience_page):
        pass

    def test_no_results_found_after_invalid_group_search(self, audience_page):
        pass

    def test_successful_group_selection(self, audience_page):
        pass

    def test_duplicate_phrases_error_message_displayed(self, audience_page):
        pass

    def test_duplicate_phrases_removed_on_click(self, audience_page):
        pass

    def test_duplicate_phrases_excluded_on_click(self, audience_page):
        pass

    def test_similar_phrases_suggestion_displayed(self, audience_page):
        pass

    def test_add_all_similar_phrases(self, audience_page):
        pass

    def test_period_search_limit_error_message_displayed(self, audience_page):
        pass

    def test_period_search_noun_form_changed(self, audience_page):
        pass

    def test_audience_card_displayed_with_correct_details(self, audience_page):
        pass"""