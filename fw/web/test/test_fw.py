import time

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
    button_change_user = (By.XPATH, '//div[contains(@class, "profileMenuButton-3D")]/..//span[@class="zen-ui-button2__content"]')
    button_context_menu = (By.XPATH, '//button[@class="ContextMenuButton"]')
    button_log_off_from_account = (By.XPATH, '//span[contains(@class, "PasspIcon_exit")]')
    button_log_off_and_delete_info_user_from_list = (By.XPATH, '//span[contains(@class, "PasspIcon_trash")]')
    button_log_in_to_another_account = (By.XPATH, '//a[@data-t="account-list-item-add"]')

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
            if self.manager.settings.time_element_Wait < index:
                return False
            preloader = self.check_is_there_element_on_the_page(Locator.preloader)
            if preloader == True:
                time.sleep(0.5)
                index = index + 0.7
            else:
                return True


    @allure.step('Возвращает текст ошибки если она есть')
    def get_reason_error_if_it_is(self):
        result = self.find_elements(Locator.error)
        if len(result) == 0:
            return self
        else:
            return self.get_tag_text(Locator.error)

    @allure.step('Нажимаем кнопку Выбрать другой')
    def click_button_change_user(self):
        self.click_element(Locator.button_change_user)
        return self

    @allure.step('Выбор пользователя для входа (среди выбранных)')
    def select_user_for_sign_in(self, login):
        time.sleep(1)
        xpath = (By.XPATH, f'//div[text()="{login}"]/../../../..//a[contains(@class, "AuthAccountListItem")]')
        self.click_element(xpath)
        return self

    @allure.step('Нажимаем на меню с действиями напротив аккаунта')
    def click_button_context_menu(self):
        self.click_element(Locator.button_context_menu)
        return self

    @allure.step('Выходим из профиля на странице авторизации')
    def log_off_from_page_authorisation(self):
        # Нажимаем на кнопку меню с действиями
        self.click_button_context_menu()
        # тайм-аут из-за анимации
        time.sleep(0.5)
        # Нажимаем на кнопку Выйти из профиля
        self.click_element(Locator.button_log_off_from_account)
        # Ожидаем, пока прелоадер прогрузится
        self.check_preloader_is_miss()
        return self

    @allure.step('Выходим из профиля и удаляем информацию о пользователе из списка')
    def log_off_and_delete_info_about_user_from_list(self):
        # Нажимаем на кнопку меню с действиями
        self.click_button_context_menu()
        # тайм-аут из-за анимации
        time.sleep(0.5)
        # Нажимаем на кнопку Выйти из профиля
        self.click_element(Locator.button_log_off_and_delete_info_user_from_list)
        return self

    @allure.step('Проверка нахождения формы ввода пароля на странице')
    def check_form_for_input_password(self):
        return self.check_is_there_element_on_the_page(Locator.input_password)

    @allure.step('Проверка нахождения формы ввода логина на странице')
    def check_form_for_input_login(self):
        return self.check_is_there_element_on_the_page(Locator.input_login)

    @allure.step('Нажимаем кнопку Войти в другой аккаунт')
    def click_button_log_in_to_another_account(self):
        self.click_element(Locator.button_log_in_to_another_account)
        return self



