from screenplay import Task, Actor, log_message
from pages.blast_off import blast_off
from pages.feature_modal import feature_modal
from actions.enter_text import enter_text
from actions.click_on import click_on
from actions.wait_for_modal import wait_for_modal



class change_feature_name(Task):
    def __init__(self, old_title, new_title):
        self.old_title = old_title
        self.new_title = new_title

    @log_message('Change the name of a Feature')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            #features = browser_for(actor).find_element(*blast_off.feature_list).find_elements_by_tag_name("li")
            #feature = for feature in features where feature.text.split('\n')[0] == self.old_title
            click_on(),
            wait_for_modal(feature_modal.title_textbox),
            enter_text(self.new_title).into(feature_modal.title_textbox),
            click_on(feature_modal.save_button)
        )

