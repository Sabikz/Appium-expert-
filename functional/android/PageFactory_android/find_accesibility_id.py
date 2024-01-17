from selenium.webdriver.common.by import By
import allure
from functional.android.settings_android import *


class Component:

    def __init__(self, value):
        self.value = value

    def find_acces_id(self, value):
        with allure.step(f'To find ACCESSIBILITY_ID {value}'):
            el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value)
            if el.is_displayed():
                return el
            else:
                print("Logo is not displayed")


    def find_id(self, value):
        with allure.step(f'To find element {value}'):
            el = driver.find_element(by=By.ID, value=value)
            return el

    def find_ids(self, value):
        with allure.step(f'To find element {value}'):
            elements = driver.find_elements(by=By.ID, value=value)
            return elements

    def find_xpath(self, value):
        with allure.step(f'To find ACCESSIBILITY_ID {value}'):
            el = driver.find_element(AppiumBy.XPATH, value)
            if el.is_displayed():
                return el
            else:
                print(f"{value} is not displayed")



