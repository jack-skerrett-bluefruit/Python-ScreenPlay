from screenplay.task import Task
from screenplay.actor import Actor
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from abilities.browse_the_web import browser_for


class _send_key_to_element(Task):
    def __init__(self, locator, key: Keys):
        self._locator = locator
        self._key = key

    def perform_as(self, actor: Actor):
        element: WebElement = browser_for(actor).find_element(*self._locator)
        element.send_keys(self._key)


def send_enter_key_to(locator):
    return _send_key_to_element(locator, Keys.ENTER)
