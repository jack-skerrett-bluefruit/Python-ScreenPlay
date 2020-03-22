from screenplay import Action, Actor, log_message
from selenium.webdriver.support.ui import Select
from abilities.browse_the_web import browser_for, waiting_browser_for
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException


class select_from_dropdown(Action):
    def __init__(self, locator, dropdown_item):
        self.locator = locator
        self.dropdown_item = dropdown_item

    @log_message('Select an element from a drop down menu')
    def perform_as(self, actor: Actor):
        def select_item_from_dropdown(browser):
            Select(browser.find_element(*self.locator)).select_by_visible_text(self.dropdown_item)
            return True

        waiting_browser_for(actor, StaleElementReferenceException).until(select_item_from_dropdown)



