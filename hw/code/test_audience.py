import pytest

from ui.pages.audience_page import AudiencePage
from base import BaseCase


class TestAudience(BaseCase):
   
    def test_audience_empty_message_displayed(self, audience_page):

        assert audience_page.is_visible_empty_message()
    
    def test_nonexistent_audience_search_displays_nothing(self, audience_page):

        audience_page.enter_search_audience("nonexistent_audience")
        assert audience_page.is_visible_zero_search_result()
    
    def test_user_list_max_length_error(self, audience_page):

        audience_page.open_user_list_tab()
        assert audience_page.is_visible_create_user_list_button()
        audience_page.click_create_user_list_button()
        assert audience_page.is_visible_title_input()
        audience_page.clear_and_enter_user_list_title((audience_page.MAX_LENGTH_TITLE+2) * 'n')
        assert audience_page.is_visible_form_error()
        assert audience_page.get_form_error() == "Превышена длина названия списка"
    
    def test_user_list_empty_title_error(self, audience_page):

        audience_page.open_user_list_tab()
        assert audience_page.is_visible_create_user_list_button()
        audience_page.click_create_user_list_button()
        assert audience_page.is_visible_title_input()
        audience_page.clear_and_enter_user_list_title('   ')
        assert audience_page.is_visible_form_error()
        assert audience_page.get_form_error() == "Обязательное поле"

    def test_user_list_default_title_generation(self, audience_page):

        audience_page.open_user_list_tab()
        assert audience_page.is_visible_create_user_list_button()
        audience_page.click_create_user_list_button()
        assert audience_page.is_visible_title_input()
        title = audience_page.get_title_data()
        assert audience_page.check_user_list_title(title)
    
    def test_audience_creation_modal_default_name(self, audience_page):
        
        assert audience_page.is_visible_create_audience_button()
        audience_page.click_create_audience_button()
        assert audience_page.is_visible_title_input()
        title = audience_page.get_title_data()
        assert audience_page.check_audience_title(title)
    
    def test_audience_name_max_length_error(self, audience_page):
        
        assert audience_page.is_visible_create_audience_button()
        audience_page.click_create_audience_button()
        audience_page.enter_audience_title((audience_page.MAX_LENGTH_TITLE+2) * 'n')
        assert audience_page.is_visible_form_error()
        assert audience_page.get_form_error() == "Максимальная длина 255 символов"
      
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

    @pytest.mark.skip #не удатся сделать спомошью js элемент input[type='file'] видимым
    def test_user_list_invalid_file_format_modal_displayed(self, audience_page):
        
        audience_page.open_user_list_tab()
        assert audience_page.is_visible_create_user_list_button()
        audience_page.click_create_user_list_button()
        assert audience_page.is_visible_user_list_type_input()
        audience_page.select_user_list_type_vk()
        audience_page.load_user_list_file("groups.xlsx")
        audience_page.click_user_list_save_button()
        assert is_visible_modale_save_file_error()

    @pytest.mark.skip #не удатся сделать спомошью js элемент input[type='file'] видимым
    def test_vk_id_list_successfully_saved(self, audience_page):

        audience_page.open_user_list_tab()
        assert audience_page.is_visible_create_user_list_button()
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