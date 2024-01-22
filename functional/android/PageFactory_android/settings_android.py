import os

import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from dotenv import load_dotenv

load_dotenv()
valid_phone = os.getenv('valid_phone')
valid_password = os.getenv('valid_password')

APPIUM_LOCAL_PORT = 4724
APPIUM_LOCAL_HOST = 'localhost'

APPIUM_PORT = 4723
APPIUM_HOST = '172.16.14.254'


custom_opts = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "12",
    "appium:deviceName": "R58M33Q95KH",
    "appium:appPackage": "kz.kmf.bankapp",
    "appium:appActivity": ".presentation.ui.view.splash.LogoActivity",
    "appium:automationName": "UiAutomator2"
})
