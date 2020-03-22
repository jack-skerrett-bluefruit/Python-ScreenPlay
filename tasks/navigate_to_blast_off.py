from screenplay import Task, Actor, log_message
from actions.click_on import click_on
from pages.side_section_bar import side_section_bar
from pages.blast_off import blast_off


class navigate_to_blast_off(Task):
    @log_message('Navigate to Blast Off')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            click_on(side_section_bar.blast_off_icon)
        )
