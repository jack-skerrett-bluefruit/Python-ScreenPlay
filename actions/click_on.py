from screenplay import Action, Actor, log_message
from abilities.browse_the_web import waiting_browser_for
from selenium.common.exceptions import StaleElementReferenceException
import time

class click_on(Action):
    def __init__(self, locator):
        self._locator = locator

    @log_message("Clicks on {self._locator[1]}")
    def perform_as(self, actor: Actor):
        def click_on_element(browser):
            browser.find_element(*self._locator).click()
            return True

        waiting_browser_for(actor, StaleElementReferenceException).until(click_on_element)
