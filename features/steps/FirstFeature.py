from behave import *
from behave import runner
from screenplay import *


# use_step_matcher("re")


class HelloAbility(Ability):
    def __init__(self):
        self.hello = "Hello world"

    def print_hello(self):
        print("      " + self.hello)


@step("Byran is an administrator")
def step_impl(context: runner.Context):
    pass

@given("Byran has added the user")
def step_impl(context: runner.Context):
    pass


@when("Hello {person}")
def step_impl(context: runner.Context, person: str):
    context.activeActor = Actor.named(person)
    context.activeActor.can(HelloAbility())
    pass

@then("the user was {user}")
def step_impl(context: runner.Context, user: str):
    context.activeActor.ability(HelloAbility).print_hello()
    assert user == context.activeActor.name, "Invalid user"

@step("there is no user")
def step_impl(context: runner.Context):
    assert not hasattr(context, 'activeActor'), "There is already a user"
    print(context.aaa)
