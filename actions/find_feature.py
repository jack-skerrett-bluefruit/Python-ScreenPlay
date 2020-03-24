from screenplay import Action, Actor, log_message
from abilities.browse_the_web import browser_for
from pages.blast_off import blast_off

class find_feature(Action):
    def __init__(self, feature_name):
        self.feature_name = feature_name

    @log_message('Find a feature called {self.feature_name}')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            feature_list_items = browser_for(actor).find_element(*blast_off.feature_list).find_elements_by_tag_name("li")
        )
