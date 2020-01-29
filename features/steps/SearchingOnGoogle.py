from behave import *
from behave import runner
from screenplay import *
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

# use_step_matcher("re")

@step(u'Byran has opened Google')
def step_impl(context):
    context.active_actor = Actor.named('Byran')
    context.browser.get('https://www.google.co.uk')


@step(u'they search for "{search_text}"')
def step_impl(context, search_text: str):
    browser: webdriver.Chrome = context.browser
    search_box: WebElement = browser.find_element_by_name('q')
    search_box.send_keys('Hello World', Keys.ENTER)
    print('hello world')

@step(u'they should see results for "{expected}" programs')
def step_impl(context, expected: str):
    pass
