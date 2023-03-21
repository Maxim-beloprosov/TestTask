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
        # Проверяем, пропал ли прелоадер
        preloader = self.APP.test_fw.check_preloader_is_miss()
        assert text_error == 'Такой логин не подойдет'
        assert preloader == True

    @allure.title('Проверка перехода на след. страницу без указания логина')
    @pytest.mark.WebTest
    def test_5(self):
        # Вводим логин
        self.APP.test_fw.input_login('')
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Проверяем, есть ли ошибка на странице
        text_error = self.APP.test_fw.get_reason_error_if_it_is()
        # Проверяем, пропал ли прелоадер
        preloader = self.APP.test_fw.check_preloader_is_miss()
        assert text_error == 'Логин не указан'
        assert preloader == True

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
        # Проверяем, пропал ли прелоадер
        preloader = self.APP.test_fw.check_preloader_is_miss()
        assert text_error == 'Недопустимый формат номера'
        assert preloader == True

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
        # Проверяем, пропал ли прелоадер
        preloader = self.APP.test_fw.check_preloader_is_miss()
        assert text_error == 'Пароль не указан'
        assert preloader == True

    @allure.title('Проверка сохранении авторизации при добавлении другого пользователя')
    @pytest.mark.WebTest
    def test_8(self):
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
        # Нажимаем кнопку "Выбрать другой"
        self.APP.test_fw.click_button_change_user()
        # Снова выбираем нужного пользователя для входа
        self.APP.test_fw.select_user_for_sign_in(login)
        # Получаем логин авторизованного пользователля
        login_authorised_user = self.APP.test_fw.get_login_authorised_user()
        assert login == login_authorised_user

    @allure.title('Проверка работоспособности кнопки "Выйти из аккаунта"')
    @pytest.mark.WebTest
    def test_9(self):
        # Вводим логин
        login = self.user['Login']
        self.APP.test_fw.input_login(self.user['Login'])
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
        # Нажимаем кнопку "Выбрать другой"
        self.APP.test_fw.click_button_change_user()
        # Нажимаем кнопку "Выйти из аккаунта"
        self.APP.test_fw.log_off_from_page_authorisation()
        # Снова выбираем нужного пользователя для входа
        self.APP.test_fw.select_user_for_sign_in(login)
        # Проверяем, есть ли на странице форма для ввода пароля
        assert self.APP.test_fw.check_form_for_input_password() == True

    @allure.title('Проверка работоспособности кнопки "Выйти и удалить из списка"')
    @pytest.mark.WebTest
    def test_10(self):
        # Вводим логин
        login = self.user['Login']
        self.APP.test_fw.input_login(self.user['Login'])
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
        # Нажимаем кнопку "Выбрать другой"
        self.APP.test_fw.click_button_change_user()
        # Нажимаем кнопку "Выйти и удалить из списка"
        self.APP.test_fw.log_off_and_delete_info_about_user_from_list()
        # Проверяем, есть ли на странице форма для ввода логина
        assert self.APP.test_fw.check_form_for_input_login() == True

    @allure.title('Проверка работоспособности кнопки "Войти в другой аккаунт"')
    @pytest.mark.WebTest
    def test_11(self):
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
        # Нажимаем кнопку "Выбрать другой"
        self.APP.test_fw.click_button_change_user()
        # Нажимаем кнопку "Войти в другой аккаунт"
        self.APP.test_fw.click_button_log_in_to_another_account()
        # Вводим логин
        login = self.user['Login']
        self.APP.test_fw.input_login(login)
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Вводим пароль
        self.APP.test_fw.input_password(self.user['Password'])
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Нажимаем кнопку профиля
        self.APP.test_fw.click_button_profile()
        # Получаем логин авторизованного пользователля
        login_authorised_user = self.APP.test_fw.get_login_authorised_user()
        assert login == login_authorised_user

    @allure.title('Ввод корректного пароля')
    @pytest.mark.WebTest
    def test_12(self):
        # Вводим логин
        email = self.user['Email']
        self.APP.test_fw.input_login(email)
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Вводим пароль
        self.APP.test_fw.input_password(self.APP.time.get_time_now_2())
        # Нажимаем кнопку Войти
        self.APP.test_fw.click_button_sign_in()
        # Проверяем, есть ли ошибка на странице
        text_error = self.APP.test_fw.get_reason_error_if_it_is()
        # Проверяем, пропал ли прелоадер
        preloader = self.APP.test_fw.check_preloader_is_miss()
        assert text_error == 'Неверный пароль'
        assert preloader == True