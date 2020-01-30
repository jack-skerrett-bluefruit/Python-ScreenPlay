from behave import runner, model
from selenium import webdriver
from screenplay.behave import *

def before_scenario(context: runner.Context, scenario: model.Scenario):
    add_screenplay_objects_to(context)
    context.actors.add_person_called('Byran')
    context.browser = webdriver.Chrome()

def after_scenario(context: runner.Context, scenario: model.Scenario):
    context.browser.quit()
