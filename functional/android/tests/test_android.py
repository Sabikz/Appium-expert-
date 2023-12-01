import allure

from functional.android.pages.auth_page import *


@allure.epic('Авторизация')
@allure.feature('Авторизация при помощи иин пользователя и номера телефона')
@allure.story('Выбрать язык приложения')
def test_auth_page():
    # Открываем страницу авторизации
    #with allure.step("Открываем страницу с локализацией"):
    auth_page.authorize()


