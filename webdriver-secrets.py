from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuration
url = "https://example.com/login"   # Replace with your target login page
username = "mveera"
password = "1234fkdjhfjsfdsj1256"

# Set up the Chrome WebDriver
driver = webdriver.Chrome()  # or use webdriver.Firefox(), etc.
driver.get(url)

# Wait for the page to load
time.sleep(2)

# Find the input fields (adjust the 'name' or 'id' selectors as needed)
username_field = driver.find_element(By.NAME, "username")  # or By.ID, etc.
password_field = driver.find_element(By.NAME, "password")

# Input credentials
username_field.send_keys(username)
password_field.send_keys(password)

# Submit the form (can be a button click or pressing Enter)
password_field.send_keys(Keys.RETURN)

# Optional: wait and close browser
time.sleep(5)
driver.quit()
