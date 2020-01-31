from screenplay.action import Action
from screenplay.actor import Actor
from tasks.enter_text import enter_text
from tasks.send_key import send_key


class search_for(Action):
    def __init__(self, text: str):
        self._text = text

    def perform_as(self, actor: Actor):
        actor.attempts_to(
            enter_text(self._text).into_textbox_with_name('q'),
            send_key.enter().to_element_with_name('q')
            )

    @staticmethod
    def text(text: str):
        return search_for(text)
