import time

from base import BaseCase


class TestSurveys(BaseCase):

    def test_check_access_redirect(self, serveys_page):
        serveys_page.open_lead_form_page()

        serveys_page.open_surveys_page()

        #assert serveys_page.get_access_accounts()