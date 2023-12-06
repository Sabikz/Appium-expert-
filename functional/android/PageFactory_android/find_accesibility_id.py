from functional.android.config_android import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import allure
from selenium.webdriver.common.by import *
from appium.webdriver.common.appiumby import *
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from functional.android.config_android import *



class TestFindByAccessibilityID:

    def __init__(self, value):
        self.value = value

    def find_acces_id(self, value):
        with allure.step(f'To find ACCESSIBILITY_ID {value}'):
            el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value)
            if el.is_displayed():
                return el
            else:
                print("Logo is not displayed")
                driver.quit()

    def find_ids(self, value):
        with allure.step(f'To find elements {value}'):
            element = driver.find_elements(by=By.ID ,value=value)
        return element

    def find_id(self, value):
        with allure.step(f'To find element {value}'):
            element = driver.find_element(by=By.ID, value=value)
        return element

    def clickable(self, value):
        with allure.step(f'element to be clickable {value}'):
            el = EC.element_to_be_clickable((By.ID, value))
            return el

    def visible(self, value):
        with allure.step(f'element to be visible {value}'):
            el = EC.visibility_of_element_located((By.ID, value))
            return el



