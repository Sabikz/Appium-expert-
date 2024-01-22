from functional.android.PageFactory_android.settings_android import *
from appium.webdriver.appium_service import AppiumService

@pytest.fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        # Check the output of `appium server --help` for the complete list of
        # server command line arguments
        args=['--address', APPIUM_LOCAL_HOST, '-p', str(APPIUM_LOCAL_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()

@pytest.fixture
def driver():
    driver = webdriver.Remote(f'http://{APPIUM_LOCAL_HOST}:{APPIUM_LOCAL_PORT}/wd/hub', options=custom_opts,
                                  direct_connection=True)
    yield driver
    driver.implicitly_wait(15)
    driver.quit()


