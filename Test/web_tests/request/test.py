import allure
import pytest

from data.settings import Settings
from Test.web_tests.web_base import WebBase


class Test(WebBase):

    user = Settings.GLOBAL['Yandex']['USERS']

    @allure.title('Вход в систему через логин и пароль')
    @pytest.mark.WebTest
    def test_1(self):
        # Вводим логин
        login = self.user['Login']
        self.APP.test_fw.input_login(login)
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Вводим пароль
        self.APP.test_fw.input_password(self.user['Password'])
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Вводим ответ на вопрос
        self.APP.test_fw.input_answer_on_special_question(self.user['Answer_on_special_question'])
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_continue()
        # Нажимаем кнопку профиля
        self.APP.test_fw.click_button_profile()
        # Получаем логин авторизованного пользователля
        login_authorised_user = self.APP.test_fw.get_login_authorised_user()
        assert login == login_authorised_user

    @allure.title('Вход в систему через почту и пароль')
    @pytest.mark.WebTest
    def test_2(self):
        # Вводим логин
        email = self.user['Email']
        self.APP.test_fw.input_login(email)
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Вводим пароль
        self.APP.test_fw.input_password(self.user['Password'])
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Вводим ответ на вопрос
        self.APP.test_fw.input_answer_on_special_question(self.user['Answer_on_special_question'])
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_continue()
        # Нажимаем кнопку профиля
        self.APP.test_fw.click_button_profile()
        # Получаем логин авторизованного пользователля
        login_authorised_user = self.APP.test_fw.get_login_authorised_user()
        assert self.user['Login'] == login_authorised_user

    @allure.title('Ввод корректного пароля, но в другом регистре')
    @pytest.mark.WebTest
    def test_3(self):
        # Вводим логин
        email = self.user['Email']
        self.APP.test_fw.input_login(email)
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Вводим пароль
        self.APP.test_fw.input_password(self.user['Password'].lower())
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Проверяем, есть ли ошибка на странице
        text_error = self.APP.test_fw.get_reason_error_if_it_is()
        assert text_error == 'Неверный пароль'

    @allure.title('Ввод некорректного логина')
    @pytest.mark.WebTest
    def test_4(self):
        # Вводим логин
        self.APP.test_fw.input_login(self.APP.time.get_time_now_2())
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Проверяем, есть ли ошибка на странице
        text_error = self.APP.test_fw.get_reason_error_if_it_is()
        assert text_error == 'Такой логин не подойдет'

    @allure.title('Проверка перехода на след. страницу без указания логина')
    @pytest.mark.WebTest
    def test_5(self):
        # Вводим логин
        self.APP.test_fw.input_login('')
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Проверяем, есть ли ошибка на странице
        text_error = self.APP.test_fw.get_reason_error_if_it_is()
        assert text_error == 'Логин не указан'

    @allure.title('Ввод некорректного номера телефона при авторизации')
    @pytest.mark.WebTest
    def test_6(self):
        # Нажимаем на кнопку Телефон
        self.APP.test_fw.click_button_phone()
        # Вводим некорректный номер телефона
        self.APP.test_fw.input_phone_number('0000000')
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Проверяем, есть ли ошибка на странице
        text_error = self.APP.test_fw.get_reason_error_if_it_is()
        assert text_error == 'Недопустимый формат номера'

    @allure.title('Проверка перехода на след. страницу без указания пароля')
    @pytest.mark.WebTest
    def test_7(self):
        # Вводим логин
        self.APP.test_fw.input_login(self.user['Login'])
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Вводим пароль
        self.APP.test_fw.input_password('')
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Проверяем, есть ли ошибка на странице
        text_error = self.APP.test_fw.get_reason_error_if_it_is()
        assert text_error == 'Пароль не указан'
