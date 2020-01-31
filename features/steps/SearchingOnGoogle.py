from behave import *
from behave import runner
from screenplay import *
from actions.search_for import search_for
from tasks.navigate import navigate
from questions.the_search import the_search
from screenplay.matchers.contains import contains
from screenplay.condition import see_that

# use_step_matcher("re")

@step(u'{actor} has opened Google')
def step_impl(context: runner.Context, actor: str):
    context.actors.switch_active(actor)
    context.they.attempts_to(
        navigate.to('https://www.google.co.uk')
        )


@step(u'they search for "{search_text}"')
def step_impl(context: runner.Context, search_text: str):
    context.they.attempts_to(
        search_for.text(search_text)
        )


@step(u"they should see a result for '{expected}'")
def step_impl(context: runner.Context, expected: str):
    context.they.should(
        see_that(the_search.result_titles(), contains(expected))
        )
