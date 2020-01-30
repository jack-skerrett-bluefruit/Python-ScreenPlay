from typing import Dict
from ..actor import Actor

class Actors:
    def __init__(self):
        self._actors: Dict[str, Actor] = {}
        self._active: Actor = None

    def __getitem__(self, key: str) -> Actor:
        return self._actors[key]

    def add_person_called(self, name: str):
        self._actors[name] = Actor.named(name)

    @property
    def active(self) -> Actor:
        return self._active

def add_screenplay_objects_to(context):
    context.actors = Actors()
