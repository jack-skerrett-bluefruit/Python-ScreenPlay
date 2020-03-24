from screenplay import Task, Actor, log_message, using
from pages.blast_off import blast_off
from pages.feature_modal import feature_modal
from pages.feature_list_item import feature_list_item
from actions.enter_text import enter_text
from actions.click_on import click_on
from actions.wait_for_modal import wait_for_modal
from actions.find_feature import find_feature



class change_feature_name(Task):
    def __init__(self, old_title, new_title):
        self.old_title = old_title
        self.new_title = new_title

    @log_message('Change the name of a Feature')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            using(find_feature(self.old_title)).as_("current_feature"),
            click_sub_element(actor.state[0], feature_list_item.edit_pencil),
            wait_for_modal(feature_modal.title_textbox),
            enter_text(self.new_title).into(feature_modal.title_textbox),
            click_on(feature_modal.save_button)
        )
