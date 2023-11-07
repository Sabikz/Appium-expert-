import allure

from functional.android.pages.auth_page import AuthPage


@allure.epic('Авторизация')
@allure.feature('Авторизация при помощи иин пользователя и номера телефона')
@allure.story('Выбрать язык приложения')
def test_auth_page():

    # Открываем страницу авторизации
    with allure.step("Открываем страницу с локализацией"):
        AuthPage.find_id(None, value='Logo')
        print("Logo")


