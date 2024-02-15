import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import screenshot
import time

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    # appPackage='com.android.settings',
    # appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_main(self) -> None:
        mobilescreen = screenshot.MobileScreen(self.driver)
        print("1")
        mobilescreen.save_screenshot_as_bmpfile()
        print("2")
        print(self.driver.current_activity)
        self.driver.activate_app("com.android.settings")
        print(self.driver.current_activity)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el.click()
        print(self.driver.current_activity)
        time.sleep(2.5)

if __name__ == '__main__':
    unittest.main()