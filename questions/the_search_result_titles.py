from screenplay import Actor, Question
from abilities.browse_the_web import browser_for

class the_search_result_titles(Question):
    def answered_by(self, actor: Actor):
        elements = browser_for(actor).find_elements_by_tag_name('h3')
        return [element.text for element in elements]
