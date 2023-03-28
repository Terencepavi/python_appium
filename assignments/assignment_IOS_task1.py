import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumIosConfig:
    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self):
        des_cap = {
            "app": "bs://53ce59a720a3b544e1aaf159b3be938d8f736452",
            "deviceName": "iPhone 11 Pro",
            "platformVersion": "13",
            "bstack:options": {
                "userName": "pavithrabalanset_Ne4foz",
                "accessKey": "pj6Zc6qpYhpdFyGqZpdn",
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test"
            }
        }

        self.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAssignment(AppiumIosConfig):
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.ID, "test-Username").send_keys("John")
        self.driver.find_element(AppiumBy.ID, "test-Password").send_keys("john123")

        self.driver.find_element(AppiumBy.ID, "test-LOGIN").click()

        actual_text = self.driver.find_element(AppiumBy.XPATH,
                                               "//XCUIElementTypeStaticText[contains(@name,'Username and password')]").get_attribute(
            "name")
        print(actual_text)

        assert_that('Username and password do not match any user in this service.').is_equal_to(actual_text)

    def test_add_to_cart(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()
