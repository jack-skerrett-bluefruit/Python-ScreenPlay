from screenplay import Task, Actor, log_message
from pages.blast_off import blast_off
from pages.feature_modal import feature_modal
from actions.enter_text import enter_text
from actions.click_on import click_on
from actions.wait_for_modal import wait_for_modal



class create_new_feature(Task):
    def __init__(self, title, description):
        self.title = title
        self.description = description

    @log_message('Create a new feature')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            click_on(blast_off.new_feature_button),
            wait_for_modal(feature_modal.title_textbox),
            enter_text(self.title).into(feature_modal.title_textbox),
            enter_text(self.description).into(feature_modal.description_textbox),
            click_on(feature_modal.save_button)
        )

