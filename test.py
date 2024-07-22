from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
chrome_options = Options()

# Setup WebDriver with ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navigate to the website
driver.get("https://python.org")

try:
    # Wait for the button to be clickable
    input_ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id-search-field"))
    )
    # Click the button once it's clickable
    input_.send_keys('pip' + Keys.ENTER)
    time.sleep(10)

except:
    # Handle cases where the button is not found or not clickable within the timeout
    print("The button with ID 'my-button' was not found or was not clickable within 10 seconds.")

# It's good practice to close the browser when done
driver.quit()
