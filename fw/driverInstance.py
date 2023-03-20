from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from data.settings import Settings


class DriverInstance:

    def __init__(self):
        self.settings = Settings

    driver = None

    def get_driver(self):
        options = webdriver.ChromeOptions()



        capabilities = DesiredCapabilities.CHROME
        capabilities['goog:loggingPrefs'] = {'browser': 'ALL',
                                             'performance': 'ALL',
                                             'server': 'ALL',
                                             'client': 'ALL'}

        if self.settings.Browser['Remote']:
            self.driver = webdriver.Remote(
                proxy=None,
                options=options,
                desired_capabilities=capabilities)
        else:
            self.driver = webdriver.Chrome(options=options, desired_capabilities=capabilities)

        if self.settings.Browser['headless'] is False:
            self.driver.maximize_window()
        return self.driver

    def stop_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
