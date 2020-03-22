from screenplay import Actor, Question
from pages.blast_off import blast_off
from abilities.browse_the_web import browser_for


class the_features_list(Question):
    def answered_by(self, actor: Actor):
        elements = browser_for(actor).find_element(*blast_off.feature_list).find_elements_by_tag_name("li")
        return [element.text.split('\n')[0] for element in elements]
