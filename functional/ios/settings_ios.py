import os

from appium.webdriver import webdriver
from dotenv import load_dotenv
from appium.options.ios import XCUITestOptions

load_dotenv()
valid_phone = os.getenv('valid_phone')
valid_password = os.getenv('valid_password')

APPIUM_PORT = 4723
APPIUM_HOST = '172.16.14.254'
APPIUM_LOCAL_HOST = 'localhost'


options = XCUITestOptions().load_capabilities({
    "platformName": "IOS",
    "appium:platformVersion": "16.3.1",
    "appium:deviceName": "Lord",
    "appium:udid": "00008030-000919540A47802E",
    "appium:app": "",
    "appium:automationName": "XCUITest"
})