from screenplay import Action, Actor, log_message
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from abilities.browse_the_web import browser_for


class _send_key_to_element(Action):
    def __init__(self, locator, key: Keys, key_name: str):
        self._locator = locator
        self._key = key
        self._key_name = key_name

    @log_message('Send key \'{self._key_name}\' to element "{self._locator}"')
    def perform_as(self, actor: Actor):
        element: WebElement = browser_for(actor).find_element(*self._locator)
        element.send_keys(self._key)


def send_enter_key_to(locator):
    return _send_key_to_element(locator, Keys.ENTER, 'Enter')
