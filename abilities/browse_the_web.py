import os
import sys
from screenplay import Ability, Actor
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.webdriver import WebDriver


class browse_the_web(Ability):
    def __init__(self, create_browser_function: type):
        self._create_browser_function = create_browser_function
        self._webdriver = None

    def clean_up(self):
        if self._webdriver is None:
            self._webdriver.quit()
            self._webdriver = None

    @property
    def browser(self) -> WebDriver:
        if self._webdriver is None:
            self._webdriver = self._create_browser_function()
        return self._webdriver

    @staticmethod
    def _create_Chrome_browser():
        chrome_options = ChromeOptions()
        if os.getenv('HEADLESS_BROWSER') != 'False':
            chrome_options.headless = True
        if sys.platform.startswith('win'):
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        return Chrome(options=chrome_options)

    @staticmethod
    def using_Chrome():
        return browse_the_web(browse_the_web._create_Chrome_browser)


def browser_for(actor: Actor) -> WebDriver:
    return actor.ability(browse_the_web).browser
