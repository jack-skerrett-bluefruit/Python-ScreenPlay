from screenplay.task import Task
from screenplay.actor import Actor
from selenium.webdriver.remote.webelement import WebElement
from abilities.browse_the_web import browser_for


class enter_text(Task):
    def __init__(self, text: str):
        self._text = text
        self._locator = None

    def perform_as(self, actor: Actor):
        element: WebElement = browser_for(actor).find_element(*self._locator)
        element.send_keys(self._text)

    def into(self, locator):
        self._locator = locator
        return self
