from appium import webdriver

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Android Emulator",
    "app": "C:\Users\acer\PycharmProjects\Appium_test\app_binaries\app-debug.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)