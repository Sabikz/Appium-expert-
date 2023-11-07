from telnetlib import EC

import allure
from appium.webdriver.common.appiumby import *
from selenium.webdriver.support.wait import WebDriverWait

from functional.android.config_android import *



class TestFindByAccessibilityID:

    def __init__(self, value):
        self.value = value

    def find_id(self, value)->None:
        with allure.step('Opening android application and find element'):
            el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value)
            assert el is not None


