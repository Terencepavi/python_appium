import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

des_cap = {
    # Set URL of the application under test
    "app" : "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",
    # Specify device and os_version for testing
    "deviceName" : "iPhone 11 Pro",
    "platformVersion" : "13",
    # Set other BrowserStack capabilities
    "bstack:options": {
        "userName" : "pavithrabalanset_Ne4foz",
        "accessKey" : "pj6Zc6qpYhpdFyGqZpdn",
        "projectName" : "First Python project",
        "buildName" : "browserstack-build-1",
        "sessionName" : "BStack first_test"
    }
}

# Initialize the remote Webdriver using BrowserStack remote URL
# and options defined above
driver = webdriver.Remote("http://hub.browserstack.com/wd/hub",desired_capabilities=des_cap)
# Test case for the BrowserStack sample iOS app.
# If you have uploaded your app, update the test case here.
text_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Button"))
)
text_button.click()
text_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
)
text_input.send_keys("hello@browserstack.com"+"\n")
time.sleep(5)
text_output = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Output"))
)
if text_output!=None and text_output.text=="hello@browserstack.com":
	assert True
else:
	assert False
# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
