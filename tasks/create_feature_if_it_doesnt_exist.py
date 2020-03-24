from screenplay import Task, Actor, log_message
from abilities.browse_the_web import browser_for
from pages.blast_off import blast_off
from actions.click_on import click_on
from pages.feature_modal import feature_modal
from actions.enter_text import enter_text
from actions.wait_for_modal import wait_for_modal
from tasks.create_new_feature import create_new_feature
from abilities.browse_the_web import waiting_browser_for
from selenium.common.exceptions import StaleElementReferenceException

class create_feature_if_it_doesnt_exist(Task):
    def __init__(self, title, description):
        self.title = title 
        self.description = description
        self.feature_not_present = True

    @log_message('Check to see if a feature of that name exists and creates a feature if it doesn\'t.')
    def perform_as(self, actor: Actor):
        def get_feature_list(browser):
            feature_list_items = browser_for(actor).find_element(*blast_off.feature_list).find_elements_by_tag_name("li")
            if(len(feature_list_items) > 0):
                for item in feature_list_items:
                    if(item.text.split('\n')[0] == self.title):
                        self.feature_not_present = False
            if(self.feature_not_present):
                    actor.attempts_to(
                        create_new_feature(self.title, self.description)
                    )
            return True

        waiting_browser_for(actor, StaleElementReferenceException).until(get_feature_list)
