import os, re

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from ui.locators.audience_locators import AudiencePageLocators
from ui.pages.base_page import BasePage

class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators()

    MAX_LENGTH_TITLE = 255

    def is_visible_empty_message(self) -> bool:
        return self.became_visible(self.locators.EMPTY_MESSAGE)
    
    def enter_search_audience(self, search_data: str):
        elem = self.find(self.locators.AUDIENCE_SEARCH_FIELD)
        elem.clear()
        elem.send_keys(search_data)
        elem.send_keys(Keys.ENTER)

    def is_visible_zero_search_result(self) -> bool:
        return self.became_visible(self.locators.ZERO_SEARCH_RESULT)

    def click_create_audience_button(self):
        self.click(self.locators.CREATE_AUDIENCE_BUTTON)

    def enter_audience_title(self, audience_title: str):
        elem = self.find(self.locators.TITLE_INPUT)
        elem.clear()
        elem.send_keys(audience_title)
        elem.send_keys(Keys.ENTER)

    def get_form_error(self) -> str:
        return self.find(self.locators.FORM_ERROR).text

    def open_user_list_tab(self):
        self.click(self.locators.USER_LIST_TAB)

    def click_create_user_list_button(self):
        self.click(self.locators.CREATE_USER_LIST_BUTTON)

    def clear_and_enter_user_list_title(self, user_list_title: str):
        elem = self.find(self.locators.TITLE_INPUT)
        elem.send_keys(Keys.CONTROL + "a")
        elem.send_keys(Keys.DELETE)
        elem.send_keys(user_list_title)
        elem.send_keys(Keys.ENTER)

    def is_visible_title_input(self) -> bool:
        return self.became_visible(self.locators.TITLE_INPUT)

    def is_visible_user_list_type_input(self) -> bool:
        return self.became_visible(self.locators.USER_LIST_TYPE_INPUT)

    def select_user_list_type_vk(self):
        elem = self.click(self.locators.USER_LIST_TYPE_INPUT)
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.ENTER)

    def load_user_list_file(self, file_name: str):
        absolute_file_path = os.path.abspath("hw/code/assets/"+file_name)
        file_input = self.find(self.locators.USER_LIST_FILE_INPUT)
        self.driver.execute_script("document.getElementsByClassName('vkuiVisuallyHidden')[0].style.visibility = 'visible';")
        file_input.send_keys(absolute_file_path)

    def click_user_list_save_button(self):
        self.click(self.locators.USER_LIST_SAVE_BUTTON)
    
    def is_visible_modale_save_file_error(self) -> bool:
        return self.became_visible(self.locators.MODAL_ERROR_SAVE_FILE)
    
    def get_title_data(self) -> str:
        return self.find(self.locators.TITLE_INPUT).get_attribute('value')

    def check_user_list_title(self, title: str) -> bool:
        regex = r"^Новый список пользователей\. \d{4}-\d{2}-\d{2} \d{2}:\d{2}$"
        return re.match(regex, title.strip()) != None

    def check_audience_title(self, title: str) -> bool:
        regex = r"^Аудитория \d{4}-\d{2}-\d{2}$"
        return re.match(regex, title.strip()) != None

    def is_visible_search_user_list_field(self) -> bool:
        return self.became_visible(self.locators.USER_LIST_SEARCH_FIELD)

    def enter_search_user_list(self, search_data: str):
        elem = self.find(self.locators.USER_LIST_SEARCH_FIELD)
        elem.clear()
        elem.send_keys(search_data)
        elem.send_keys(Keys.ENTER)

    def is_visible_user_list_title_input(self) -> bool:
        return self.became_visible(self.locators.TITLE_INPUT)

    def get_title_length(self) -> int:
        data = self.find(self.locators.TITLE_LENGTH).text
        return int(re.split('/', data)[0].strip())

    def is_visible_create_audience_button(self) -> bool:
        return self.became_visible(self.locators.CREATE_AUDIENCE_BUTTON)

    def is_visible_selector_conditional_button(self) -> bool:
        return self.became_visible(self.locators.SELECTOR_CONDITIONAL_BUTTON)

    def get_current_selector_conditional_button(self) -> str:
        return self.find(self.locators.SELECTOR_CONDITIONAL_BUTTON).text

    def calculate_next_condition(self, current: str) -> str:
        conditions = ['всем условиям', 'хотя бы одному из условий', 'ни одному из условий']
        index = conditions.index(current)
        return conditions[(index+1) % 3]

    def click_selector_conditional_button(self):
        self.click(self.locators.SELECTOR_CONDITIONAL_BUTTON)

    def select_conditional(self, condition: str):
        self.click(self.locators.SELECT_CONDITION(condition))

    def click_close_icon(self):
        self.click(self.locators.CLOSE_ICON)

    def is_visible_warning_modal(self) -> bool:
        return self.became_visible(self.locators.WARNING_MODEL)
    
