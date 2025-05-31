from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element("name", "q")
search_box.send_keys("QA automation with Python")
search_box.send_keys(Keys.RETURN)

time.sleep(2)

assert "QA" in driver.page_source

print("Test Passed: 'QA' found in search results.")

driver.quit()







Add my first automation test
