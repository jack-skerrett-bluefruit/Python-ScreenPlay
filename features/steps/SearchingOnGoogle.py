from behave import *
from behave import runner
from screenplay import *
from screenplay.matchers.contains import contains
from screenplay.condition import see_that
from actions.search_for import search_for
from tasks.navigate_to import navigate_to
from questions.the_search_result_titles import the_search_result_titles

# use_step_matcher("re")

@step(u'{actor} has opened Google')
def step_impl(context: runner.Context, actor: str):
    context.actors.switch_active(actor)
    context.they.attempts_to(
        navigate_to('https://www.google.co.uk')
        )


@step(u'they search for "{search_text}"')
def step_impl(context: runner.Context, search_text: str):
    context.they.attempts_to(
        search_for(search_text)
        )


@step(u"they should see a result for '{expected}'")
def step_impl(context: runner.Context, expected: str):
    context.they.should(
        see_that(the_search_result_titles(), contains(expected))
        )
