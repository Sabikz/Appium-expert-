import os

from appium.webdriver import webdriver
from dotenv import load_dotenv
from appium.options.ios import XCUITestOptions

load_dotenv()
valid_phone = os.getenv('valid_phone')
valid_password = os.getenv('valid_password')

APPIUM_PORT = 4724
APPIUM_HOST = '172.16.14.254'
APPIUM_LOCAL_HOST = 'localhost'


options = XCUITestOptions().load_capabilities({
    'platformVersion': '13.4',
    'deviceName': 'iPhone Simulator',
    'app': '/full/path/to/app/UICatalog.app.zip',
})