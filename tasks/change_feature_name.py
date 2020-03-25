from screenplay import Task, Actor, log_message, using
from pages.blast_off import blast_off
from pages.feature_modal import feature_modal
from pages.feature_list_item import feature_list_item
from actions.enter_text import enter_text
from actions.clear_text import clear_text
from actions.click_on import click_on
from actions.find_feature import find_feature
from actions.click_sub_element import click_sub_element
from actions.click_element import click_element
from actions.find_feature import find_feature
import time


class change_feature_name(Task):
    def __init__(self, old_title, new_title):
        self.old_title = old_title
        self.new_title = new_title

    @log_message('Change the name of a Feature')
    def perform_as(self, actor: Actor):
        time.sleep(1) # this shouldnt be here but I dont know how to make it better. I could try and wrap the using in one of those wait until dudes but I dont really understand how the code works and I feel like im just going in circles, trapped in a goldfish bowl of my own ignorance and its no fun
        actor.attempts_to(
            using(find_feature(self.old_title)).as_("current_feature")
        )       
        actor.attempts_to(
            click_element(actor.state['current_feature']),
            click_sub_element(actor.state['current_feature'], feature_list_item.edit_pencil),
            clear_text(feature_modal.title_textbox),
            enter_text(self.new_title).into(feature_modal.title_textbox),
            click_on(feature_modal.save_button)
        )
        time.sleep(1) # another stupid sleep needed because im too thick to figure it out
