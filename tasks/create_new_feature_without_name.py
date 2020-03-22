from screenplay import Task, Actor, log_message
from actions.click_on import click_on
from actions.wait_for_modal import wait_for_modal
from actions.enter_text import enter_text
from pages.blast_off import blast_off
from pages.feature_modal import feature_modal

class create_new_feature_without_name(Task):
    @log_message('Enter a description of what the task does')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            click_on(blast_off.new_feature_button),
            wait_for_modal(feature_modal.title_textbox),
            enter_text("").into(feature_modal.title_textbox),
            click_on(feature_modal.save_button)
        )
