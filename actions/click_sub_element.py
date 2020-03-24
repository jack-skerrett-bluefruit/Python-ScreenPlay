from screenplay import Action, Actor, log_message
from actions.click_on import click_on

class click_sub_element(Action):
    def __init__(self, element, subelement):
        self.element = element
        self.subelement = subelement
        
    @log_message('Clicks on a sub element')
    def perform_as(self, actor: Actor):
        