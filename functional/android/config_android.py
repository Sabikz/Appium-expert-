import pytest

from appium.webdriver.appium_service import AppiumService
from functional.android.settings_android import *


@pytest.fixture(scope='function')
def appium_driver(request):
    driver = initialize_appium_driver()

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver





