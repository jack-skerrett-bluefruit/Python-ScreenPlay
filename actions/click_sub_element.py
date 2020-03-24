from screenplay import Action, Actor, log_message
from selenium.webdriver.remote.webdriver import WebElement
from abilities.browse_the_web import waiting_browser_for
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

class click_sub_element(Action):
    def __init__(self, element, subelement):
        self.element : WebElement = element 
        self.subelement = subelement
        
    @log_message('Clicks on a sub element')
    def perform_as(self, actor: Actor):
        def click_on_element(browser):
            self.element.find_element(*self.subelement).click()
            return True

        waiting_browser_for(actor, NoSuchElementException).until(click_on_element)
        
