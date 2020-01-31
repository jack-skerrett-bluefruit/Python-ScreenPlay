from screenplay import Action, Actor
from tasks.enter_text import enter_text
from tasks.send_key import send_enter_key_to_element_with_name


class search_for(Action):
    def __init__(self, text: str):
        self._text = text

    def perform_as(self, actor: Actor):
        actor.attempts_to(
            enter_text(self._text).into_textbox_with_name('q'),
            send_enter_key_to_element_with_name('q')
            )
