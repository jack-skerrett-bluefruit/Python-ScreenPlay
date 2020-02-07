from typing import List
from .ability import Ability
from .condition import Condition
from .task_or_action import TaskOrAction
from .log import Log


class Actor:
    def __init__(self, name: str):
        self.name = name
        self.abilities: List[Ability] = []

    @staticmethod
    def named(name: str):
        return Actor(name)

    def clean_up(self):
        for ability in self.abilities:
            ability.clean_up()

    def can(self, *abilities: Ability):
        self.abilities.extend(abilities)

    def ability(self, ability_type: type):
        for ability in self.abilities:
            if isinstance(ability, ability_type):
                return ability
        assert False, "Actor " + self.name + " does not have ability '" + ability_type.__name__ + "'"

    def attempts_to(self, *tasks_or_actions: TaskOrAction):
        if len(tasks_or_actions) > 0:
            Log.increment_level()
            for task_or_action in tasks_or_actions:
                task_or_action.perform_as(self)
            Log.decrement_level()

    def should(self, *conditions: Condition):
        if len(conditions) > 0:
            for condition in conditions:
                condition.check_as(self)
