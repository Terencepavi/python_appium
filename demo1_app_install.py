import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    "platformName": "android",
    "deviceName": "oneplus",
    "app": r"C:\APK\khan-academy-7-3-2.apk"
}

driver=webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=des_cap)
get_dismiss_button = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")
# if len(get_dismiss_button) > 0:
#     get_dismiss_button[0].click()
time.sleep(5)
get_dismiss_button.click()
time.sleep(5)
driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[contains(@content-desc,'username')]").send_keys('abc@xyz.com')
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Password']").send_keys('abc@xyz')

print(driver.page_source)

time.sleep(5)
driver.quit()

print(driver.page_source)

time.sleep(5)
driver.quit()