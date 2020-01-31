from typing import List
from screenplay.question import Question
from screenplay import Actor
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from abilities.browse_the_web import browse_the_web

class the_search(Question):
    def answered_by(self, actor: Actor):
        browser: WebDriver = actor.ability(browse_the_web).browser
        elements: List[WebElement] = browser.find_elements_by_tag_name('h3')
        return [element.text for element in elements]

    @staticmethod
    def result_titles():
        return the_search()
