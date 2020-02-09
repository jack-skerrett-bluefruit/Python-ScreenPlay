from screenplay import Action, Actor, log_message
from abilities.browse_the_web import browser_for

class navigate_to(Action):
    def __init__(self, url: str):
        self._url = url

    @log_message('Navigate browser to \'{self._url}\'')
    def perform_as(self, actor: Actor):
        browser_for(actor).get(self._url)
