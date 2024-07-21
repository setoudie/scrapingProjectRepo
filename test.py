from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print("Here the sample test case will be started")
driver = webdriver.Chrome()
# Here, this statement is used to maximize the window size
driver.maximize_window()
# Here, this statement is used to navigate to the url
driver.get("https://www.google.com/")
driver.find_element(by=By.NAME, value='q').send_keys('javafont')
# Here, we have to identify the Google search text box and enter the value
time.sleep(13)  # here, the system will remain in sleep for 13sec
# After done with the process click on the Google search button
driver.find_element(by=By.NAME, value="btnK").send_keys(Keys.ENTER)
time.sleep(13)  # here, the system will remain in sleep for 13sec
# Here, we are trying to close the browser
driver.close()
print("sample test case successfully completed")
