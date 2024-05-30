import pytest

from ui.pages.audience_page import AudiencePage
from base import BaseCase


class TestAudience(BaseCase):

    #@pytest.mark.skip
    def test_audience_empty_message_displayed(self, audience_page):
        assert audience_page.is_visible_empty_message()

    def test_nonexistent_audience_search_displays_nothing(self, audience_page):
        pass

    def test_user_list_max_length_error(self, audience_page):
        pass

    def test_user_list_empty_name_error(self, audience_page):
        pass

    def test_user_list_invalid_file_format_modal_displayed(self, audience_page):
        pass

    def test_user_list_default_name_generation(self, audience_page):
        pass

    def test_vk_id_list_successfully_saved(self, audience_page):
        pass

    def test_audience_creation_modal_default_name(self, audience_page):
        pass

    def test_audience_name_max_length_error(self, audience_page):
        pass

    def test_audience_name_character_count_displayed(self, audience_page):
        pass

    def test_change_matching_condition_modal_displayed(self, audience_page):
        pass

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
        pass