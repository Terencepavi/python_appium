from appium.webdriver.common.appiumby import AppiumBy

import time

import pytest
from appium import webdriver


class AppiumConfig:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def config(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "app": r"C:\APK\hyundai_app.apk"
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(20)

        yield
        time.sleep(5)


'''Need to handle allow popups'''
class TestHyundai(AppiumConfig):
    def test_sign_up(self):
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/txt_signup").click()
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtFullname").send_keys('Johnwick')
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtMobileNumber").send_keys(
            '9876543210')
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtEmailAddress").send_keys(
            'test@gmail.com')
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtPasswordRegis").send_keys('test@gmail.com')
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/edtConfirmedPasswordRegis").send_keys('Qqwety@1234@')
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/checkAcceptTermsCondition").click()
        self.driver.find_element(AppiumBy.ID, "com.bsl.hyundai:id/btnRegisterOnRegis").click()
