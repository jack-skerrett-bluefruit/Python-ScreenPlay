from screenplay import Action, Actor, log_message
from abilities.browse_the_web import browser_for, waiting_browser_for
from selenium.common.exceptions import NoSuchElementException


class wait_for_modal(Action):
    def __init__(self, locator):
            self._locator = locator

    @log_message("Waits for a modal to display")
    def perform_as(self, actor: Actor):

        def modal_is_displayed(browser):
            browser.find_element(*self._locator)
            return True

        waiting_browser_for(actor, NoSuchElementException).until(modal_is_displayed)
