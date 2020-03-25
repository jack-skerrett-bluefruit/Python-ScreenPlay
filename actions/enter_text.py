"""Action class to enter text into a webpage element"""

from screenplay import Action, Actor, log_message
from selenium.webdriver.remote.webelement import WebElement
from abilities.browse_the_web import browser_for, waiting_browser_for
from selenium.common.exceptions import NoSuchElementException


class enter_text(Action):
    """
    Creates an Action class to enter text into a webpage element.
    Need to call the 'into' method to specify the element.

    e.g. enter_text('Hello').into(textbox)

    Arguments:

    text - The text to send to the webpage element
    """
    def __init__(self, text: str):
        self._text = text
        self._locator = None

    @log_message('Enter text \'{self._text}\' into element "{self._locator}"')
    def perform_as(self, actor: Actor):
        def entering_text(browser):
            element: WebElement = browser_for(actor).find_element(*self._locator)
            element.send_keys(self._text)
            return True
        waiting_browser_for(actor, (NoSuchElementException)).until(entering_text)

    def into(self, locator):
        """
        Specifies the element to enter the text into

        Arguments:

        locator - A tuple with the first element is a selenium By value and
        the second a string to specify the id/tag/etc...
        """
        self._locator = locator
        return self
