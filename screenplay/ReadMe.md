# Screen Play Pattern for Python

![Class diagram](class_diagram.png)

## Ability

``` python
from screenplay import Ability, Actor

class interact_with_the_system(Ability):
	def __init__(self):
		# Initialise object (optional)

	def clean_up(self):
		# Clean up, called when the Actor who
		# has the ability is no longer required
```

## Actor

``` python
from screenplay import Actor

actor = Actor.named('bob')
actor.can(interact_with_the_system())
```

**NOTE - This is not how an actor is normally created.
Normally you would use the `Actors.add_person_called(...)` method.**