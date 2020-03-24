from screenplay import Action, Actor, log_message

class click_element(Action):
    def __init__(self, element):
        self.element = element

    @log_message("Clicks on element")
    def perform_as(self, actor: Actor):
        self.element.click()
