from screenplay import Task, Actor, log_message
from actions.click_on import click_on
from pages.feature_modal import feature_modal


class save_feature(Task):
    @log_message('Save the current feature')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            click_on(feature_modal.save_button)
        )
