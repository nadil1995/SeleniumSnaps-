from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait

# Set the location of the Chrome browser

driver_path = os.path.join(os.getcwd(), "imp", "msedgedriver") 
driver = webdriver.Edge(executable_path=driver_path)


# Navigate to the URL
driver.get("https://mail.yahoo.com/")
time.sleep(10)
# Locate the web element

logo = driver.find_element(By.CLASS_NAME,'rightContainer')

# Capture screenshot with the Screenshot method
screenshot_path = "D:\\Venvs\\Snaping Security Monioring\\SeleniumSnaps-\\Screenshots\\logoScreenshot2.png"
logo.screenshot(screenshot_path)

driver.quit()
