from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium with Python")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

# Print page title
print(driver.title)

# Close the browser
driver.quit()
