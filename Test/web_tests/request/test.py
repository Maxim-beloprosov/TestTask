import time
from selenium.webdriver.common.by import By
import allure
import pytest

from Test.web_tests.web_base import WebBase


class Test(WebBase):

    @allure.title('Переходим на сайт Apple')
    @pytest.mark.WebTest
    def test_go_to_apple(self):
        for i in range(1, 21):
            locator1 = (By.XPATH, '//div[@role="button"]')
            count = len(self.APP.web_base.find_elements(locator1))
            x = count - 1
            locator2 = (By.XPATH, f'//div[@role="button"][{x}]')
            self.APP.web_base.right_click(locator2)
            time.sleep(1)
            locator3 = (By.XPATH, f'//div[@data-text-as-pseudo-element="Выйти"]')
            self.APP.web_base.click_element(locator3)
            time.sleep(1)
            locator4 = (By.XPATH, f'//div[@data-text-as-pseudo-element="Подтвердить"]')
            self.APP.web_base.click_element(locator4)
            time.sleep(5)