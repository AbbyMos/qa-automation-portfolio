from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Open Chrome and go to Google
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Find the search box and search for "QA automation with Python"
search_box = driver.find_element("name", "q")
search_box.send_keys("QA automation with Python")
search_box.send_keys(Keys.RETURN)

# Wait a little and check results
time.sleep(2)

assert "QA" in driver.page_source

print("Test Passed: 'QA' found in search results.")

# Close the browser
driver.quit()






Add my first automation test
