from behave import *
from behave import runner
from screenplay import *
from actions.search_for import search_for
from tasks.navigate import navigate

# use_step_matcher("re")

@step(u'{actor} has opened Google')
def step_impl(context: runner.Context, actor: str):
    context.actors.switch_active(actor)
    context.actors.active.attempts_to(
        navigate.to('https://www.google.co.uk')
        )


@step(u'they search for "{search_text}"')
def step_impl(context: runner.Context, search_text: str):
    context.actors.active.attempts_to(
        search_for.text(search_text)
        )


@step(u'they should see results for "{expected}" programs')
def step_impl(context: runner.Context, expected: str):
    pass
