from behave import runner, model
from selenium import webdriver

def before_scenario(context: runner.Context, scenario: model.Scenario):
    context.actors = {}
    context.actors['hello'] = "World"
    context.browser = webdriver.Chrome()

def after_scenario(context: runner.Context, scenario: model.Scenario):
    context.browser.quit()
