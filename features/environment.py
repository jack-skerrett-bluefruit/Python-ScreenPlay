from behave import runner
from selenium import webdriver

def before_all(context : runner.Context):
    print('all')
    context.aaa = 'helen'

    context.browser = webdriver.Chrome()

def after_all(context: runner.Context):
    context.browser.quit()
