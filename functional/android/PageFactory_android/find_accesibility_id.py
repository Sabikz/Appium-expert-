import time
from telnetlib import EC

import allure
from appium.webdriver.common.appiumby import *
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from functional.android.config_android import *



class TestFindByAccessibilityID:

    def __init__(self, value):
        self.value = value

    def find_acces_id(self, value):
        with allure.step(f'Opening android application and find ACCESSIBILITY_ID {value}'):
            el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value)
            assert el is not None

    def find_id(self, value, wait=1, by=By.ID):
        with allure.step(f'Opening android application and find ID {value}'):
            while True:
                try:
                    element = driver.find_element(by=by, value=value)
                    break
                except NoSuchElementException:
                    time.sleep(wait)
            return element


