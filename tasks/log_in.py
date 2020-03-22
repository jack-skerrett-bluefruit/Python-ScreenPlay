from screenplay import Task, Actor, log_message
from pages.login_page import login_page
from actions.enter_text import enter_text
from actions.click_on import click_on
from pages.nav_header import nav_header


class log_in(Task):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @log_message('Log in to Mission Control')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            enter_text(self.username).into(login_page.username_textbox),
            enter_text(self.password).into(login_page.password_textbox),
            click_on(login_page.log_in_button)
        )
