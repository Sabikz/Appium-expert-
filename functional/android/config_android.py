import pytest

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from functional.android.settings_android import *


@pytest.fixture(scope='function')
def appium_service():
    service = AppiumService()
    service.start(
        # Check the output of `appium server --help` for the complete list of
        # server command line arguments
        args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()

def create_android_driver(*args):
    global driver
    if custom_opts is not None:
        driver = webdriver.Remote('http://localhost:4724/wd/hub', options=custom_opts, direct_connection=True)
    if options_dev is not None:
        driver = webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub', options=options_dev, direct_connection=True)
    return driver

driver = create_android_driver(custom_opts, options_dev)