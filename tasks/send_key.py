from screenplay.task import Task
from screenplay.actor import Actor
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from abilities.browse_the_web import browse_the_web


class _send_key_to_element_with_id_task(Task):
    def __init__(self, id: str, key: Keys):
        self._id = id
        self._key = key

    def perform_as(self, actor: Actor):
        element: WebElement = actor.ability(browse_the_web).browser.find_element_by_id(self._id)
        element.send_keys(self._key)


class _send_key_to_element_with_name_task(Task):
    def __init__(self, name: str, key: Keys):
        self._name = name
        self._key = key

    def perform_as(self, actor: Actor):
        element: WebElement = actor.ability(browse_the_web).browser.find_element_by_name(self._name)
        element.send_keys(self._key)


class send_key:
    def __init__(self, key: Keys):
        self._key = key

    def to_element_with_id(self, id: str):
        return _send_key_to_element_with_id_task(id, self._key)

    def to_element_with_name(self, name: str):
        return _send_key_to_element_with_name_task(name, self._key)

    @staticmethod
    def enter():
        return send_key(Keys.ENTER)
