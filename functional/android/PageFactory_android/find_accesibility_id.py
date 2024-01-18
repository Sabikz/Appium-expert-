import time

import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pyautogui
from functional.android.settings_android import *


class Component:

    def __init__(self, value):
        self.value = value

    def find_acces_id(self, value):
        el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value)
        if el.is_displayed() is True:
            return el
        else:
            pass


    def find_xpath(self, value):
        try:
            # el = driver.find_element(AppiumBy.XPATH, value)
            el = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, value)))
            assert el.is_displayed() is True
            return el
        except TimeoutException:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'functional\android.\Screenshot\screenshot_1.png')
            print('Loading took too much time')
