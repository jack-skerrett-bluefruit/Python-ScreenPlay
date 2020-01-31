from screenplay.task import Task
from screenplay.actor import Actor
from abilities.browse_the_web import browser_for

class navigate(Task):
    def __init__(self, url: str):
        self._url = url

    def perform_as(self, actor: Actor):
        browser_for(actor).get(self._url)

    @staticmethod
    def to(url: str):
        return navigate(url)
