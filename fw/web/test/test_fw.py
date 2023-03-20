import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import allure

from fw.web.web_base import WebBase


class Locator:
    input_login = (By.XPATH, '//input[@name="login"]')
    button_sign_in = (By.XPATH, '//button[@id="passp:sign-in"]')
    button_continue = (By.XPATH, '//button[@type="submit"]')
    input_password = (By.XPATH, '//input[@name="passwd"]')
    input_answer_on_special_question = (By.XPATH, '//input[@name="question"] ')
    button_profile = (By.XPATH, '//div[contains(@class, "profileMenuButton")]')
    name_authorised_user = (By.XPATH, '//div[@class="ask-user-permissions-content__displayName-dY"]')
    error = (By.XPATH, '//div[contains(@class,  "error")]')
    preloader = (By.XPATH, '//div[contains(@class, "Spin2_progress")]')
    button_phone = (By.XPATH, '//button[@data-type="phone"]')
    input_phone_number = (By.XPATH, '//input[contains(@class, "Textinput-Control_phone")]')


class TestFW(WebBase):

    @allure.step('Нажимаем на кнопку Телефон')
    def click_button_phone(self):
        self.click_element(Locator.button_phone)
        return self

    @allure.step('Вводим логин')
    def input_login(self, text):
        self.send_keys(Locator.input_login, text)
        return self

    @allure.step('Вводим номер телефона')
    def input_phone_number(self, text):
        self.send_keys(Locator.input_phone_number, text)
        return self

    @allure.step('Нажимаем кнопку Войти')
    def click_button_sign_in(self):
        self.click_element(Locator.button_sign_in)
        return self

    @allure.step('Нажимаем кнопку Продолжить')
    def click_button_continue(self):
        self.click_element(Locator.button_continue)
        return self

    @allure.step('Вводим пароль')
    def input_password(self, text):
        self.send_keys(Locator.input_password, text)
        return self

    @allure.step('Вводим ответ на секретный вопрос')
    def input_answer_on_special_question(self, text):
        self.send_keys(Locator.input_answer_on_special_question, text)
        return self

    @allure.step('Нажимаем на кнопку профиль')
    def click_button_profile(self):
        self.click_element(Locator.button_profile)
        return self

    @allure.step('Получаем логин авторизованного пользователя')
    def get_login_authorised_user(self):
        return self.get_tag_text(Locator.name_authorised_user)

    @allure.step('Проверка что прелоадер пропал, если нет - отдаем False')
    def check_preloader_is_miss(self):
        index = 0
        while True:
            try:
                if self.manager.settings.time_element_Wait < index:
                    return False
                preloader = self.find_elements(Locator.preloader)
                if len(preloader) > 0:
                    time.sleep(0.5)
                    index = index + 0.7
                else:
                    return False
            except NoSuchElementException:
                return False

    @allure.step('Возвращает текст ошибки ессли она есть')
    def get_reason_error_if_it_is(self):
        result = self.find_elements(Locator.error)
        if len(result) == 0:
            return self
        else:
            return self.get_tag_text(Locator.error)

