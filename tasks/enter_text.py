from screenplay.task import Task
from screenplay.actor import Actor
from selenium.webdriver.remote.webelement import WebElement
from abilities.browse_the_web import browse_the_web

class _enter_text_into_element_with_id_task(Task):
    def __init__(self, id: str, text: str):
        self._id = id
        self._text = text

    def perform_as(self, actor: Actor):
        element: WebElement = actor.ability(browse_the_web).browser.find_element_by_id(self._id)
        element.send_keys(self._text)

class _enter_text_into_element_with_name_task(Task):
    def __init__(self, name: str, text: str):
        self._name = name
        self._text = text

    def perform_as(self, actor: Actor):
        element: WebElement = actor.ability(browse_the_web).browser.find_element_by_name(self._name)
        element.send_keys(self._text)


class enter_text:
    def __init__(self, text: str):
        self._text = text

    def into_textbox_with_id(self, id: str):
        return _enter_text_into_element_with_id_task(id, self._text)

    def into_textbox_with_name(self, name: str):
        return _enter_text_into_element_with_name_task(name, self._text)
