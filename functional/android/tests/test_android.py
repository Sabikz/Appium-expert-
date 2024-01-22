import allure
import pytest

from functional.android.pages.base_page import *


@allure.parent_suite('Прохождение onboarding')
@allure.suite('Регистрация')
@allure.sub_suite('Успешная первичная регистрация при выборе языка русский')
@allure.title("Проверка атрибутов главной страницы при выборе языка русский")
def test_auth_page(driver):
    base_page.main_page(driver, 'ru')









