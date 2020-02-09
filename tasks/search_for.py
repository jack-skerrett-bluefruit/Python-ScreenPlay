from screenplay import Task, Actor, log_message
from actions.enter_text import enter_text
from actions.send_key import send_enter_key_to
from pages.google_homepage import google_homepage


class search_for(Task):
    def __init__(self, text: str):
        self._text = text

    @log_message('Enter \'{self._text}\' into google')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            enter_text(self._text).into(google_homepage.search_textbox),
            send_enter_key_to(google_homepage.search_textbox)
            )
