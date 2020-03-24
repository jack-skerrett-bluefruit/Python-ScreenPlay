from screenplay import Action, Actor, log_message
from abilities.browse_the_web import waiting_browser_for
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

class clear_text(Action):
    def __init__(self, locator):
        self._locator = locator

    @log_message("Clears text {self._locator[1]}")
    def perform_as(self, actor: Actor):
        def clear_element_text(browser):
            browser.find_element(*self._locator).clear()
            return True

        waiting_browser_for(actor, (StaleElementReferenceException, NoSuchElementException)).until(clear_element_text)
