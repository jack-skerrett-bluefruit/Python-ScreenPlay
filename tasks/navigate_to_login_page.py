from screenplay import Task, Actor, log_message
from actions.click_on import click_on
from pages.nav_header import nav_header

class navigate_to_login_page(Task):
    @log_message('Navigate to the login page')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            click_on(nav_header.login_link)
        )

