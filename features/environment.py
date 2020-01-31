from behave import runner, model
from selenium import webdriver
from screenplay.behave import *
from abilities.browse_the_web import browse_the_web


def before_scenario(context: runner.Context, scenario: model.Scenario):
    add_screenplay_objects_to(context)
    context.actors.add_person_called('Byran')
    context.actors['Byran'].can(browse_the_web.using_Chrome())


def after_scenario(context: runner.Context, scenario: model.Scenario):
    context.actors.clean_up()
