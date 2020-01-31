from screenplay.ability import Ability
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver


class browse_the_web(Ability):
    def __init__(self, browserType: type):
        self._browserType = browserType
        self._webdriver = None

    def clean_up(self):
        if self._webdriver != None:
            self._webdriver.quit()

    @property
    def browser(self) -> WebDriver:
        if self._webdriver == None:
            self._webdriver = self._browserType()
        return self._webdriver

    @staticmethod
    def using_Chrome():
        return browse_the_web(Chrome)
