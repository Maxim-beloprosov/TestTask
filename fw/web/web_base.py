from fw.fw_base import FWBase
from time import sleep

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class WebBase(FWBase):

    def GetDriver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.get_driver()
        return self.manager.driver_instance.driver

    def allure_screenshot(self):
        try:
            allure.attach(self.GetDriver().get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(str(e))

    @allure.step('Open main page')
    def open_main_page(self):
        main_page = self.manager.settings.GLOBAL[self.manager.settings.branch]['main_page']
        title = self.GetDriver().title
        if main_page not in title:
            self.GetDriver().get(main_page)


    @allure.step('click')
    def click_element(self, locator):
        try:
            web_element = self.find_element(locator)
            web_element.click()

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

    @allure.step('Send keys')
    def send_keys(self, locator, text):
        try:
            web_element = self.find_element(locator)
            web_element.send_keys(text)

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)


    def get_tag_text(self, locator):
        try:
            text = self.find_element(locator).text
            return text
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    def scroll_to_element(self, locator):
        try:
            element = self.find_element(locator).location_once_scrolled_into_view
            script = "window.scrollBy(" + str(element['x'] - 180) + ", " + str(element['y'] - 180) + ")"
            self.GetDriver().execute_script(script)
        except StaleElementReferenceException as e:
            self.allure_ElementNotVisibleException(e)


    @allure.step('screenshot')
    def allure_screenshot(self):
        try:
            allure.attach(self.GetDriver().get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(str(e))


    # остановщик теста при ошибке
    @allure.step('ElementNotVisibleException')
    def allure_ElementNotVisibleException(self, exeption_text):
        self.allure_screenshot()
        assert True == False

    # остановщик теста при ошибке
    @allure.step('NoSuchElementException')
    def allure_NoSuchElementException(self, exeption_text):
        self.allure_screenshot()
        assert True == False

    # остановщик теста при ошибке
    @allure.step('StaleElementReferenceException')
    def allure_StaleElementReferenceException(self, exeption_text):
        assert True == False

    def find_element(self, locator, wait=None):
        if wait is None:
            wait = self.manager.settings.time_element_Wait
        try:
            web_element = WebDriverWait(self.GetDriver(), wait).until(EC.presence_of_element_located(locator))
            return web_element
        except:
            self.allure_screenshot()
            raise

    def find_elements(self, locator):
        try:
            return WebDriverWait(self.GetDriver(), self.manager.settings.time_element_Wait).until(EC.presence_of_all_elements_located(locator))
        except:
            self.allure_screenshot()
            raise

    @allure.step('Проверяем, есть ли элемент на странице')
    def check_is_there_element_on_the_page(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

