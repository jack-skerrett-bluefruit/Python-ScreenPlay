from behave import given, when, then
from tasks.navigate_to_mission_control_home import navigate_to_mission_control_home
from tasks.navigate_to_login_page import navigate_to_login_page
from tasks.log_in import log_in
from tasks.select_project import select_project
from tasks.navigate_to_blast_off import navigate_to_blast_off
from tasks.create_new_feature import create_new_feature
from tasks.create_new_feature_without_name import create_new_feature_without_name
from pages.nav_header import nav_header
from screenplay.condition import see_that
from screenplay.matchers.contains import contains
from questions.the_features_list import the_features_list
from tasks.change_feature_name import change_feature_name
from tasks.create_feature_if_it_doesnt_exist import create_feature_if_it_doesnt_exist
from tasks.save_feature import save_feature
from actions.click_on import click_on



@given(u'I am viewing Blast Off')
def step_impl(context):
    context.they.attempt_to(
        navigate_to_mission_control_home(),
        navigate_to_login_page(),
        log_in(username = "mission.control.tester@bluefruit.co.uk", password = "MissionControlTester123@"),
        select_project("Test Project"),
        navigate_to_blast_off()
    )

@when(u'I add a new feature called "{title}"')
def step_impl(context, title):
    context.they.attempt_to(
        create_new_feature(title = title, description = "THIS WAS WRITTEN AUTOMATICALLY" )
    )


@then(u'"{title}" is in the list of features')
def step_impl(context, title):
    context.they.should(
        see_that(the_features_list(), contains(title))
    )


@when(u'I add a new Feature without a name')
def step_impl(context):
    context.they.attempt_to(
        create_new_feature_without_name()
    )


@then(u'no new Feature is in the Feature list')
def step_impl(context):
    context.they.should(
        #see_that(the_features_list(), does_not_contain(""))
    )


@given(u'the feature "{title}" exists')
def step_impl(context, title):
    context.they.attempt_to(
        create_feature_if_it_doesnt_exist(title, "Test")
    )


@when(u'"{old_title}" is changed to "{new_title}" and saved')
def step_impl(context, old_title, new_title):
    context.they.attempt_to(
        change_feature_name(old_title, new_title)
    )


@then(u'the feature name is "{title}"')
def step_impl(context, title):
    context.they.should(
        see_that(the_features_list(), contains(title)),
    )
