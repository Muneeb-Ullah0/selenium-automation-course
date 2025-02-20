from selenium import webdriver
import time

driver = webdriver.Chrome()

# Open the first website
driver.get("https://www.example.com")

# Open a new window using JavaScript
driver.execute_script("window.open('https://www.google.com');")

# Get window handles
windows = driver.window_handles
print("Windows:", windows)

# Switch to the new window
driver.switch_to.window(windows[1])
print("Switched to:", driver.title)

# Switch back to the first window
driver.switch_to.window(windows[0])
print("Switched back to:", driver.title)

# Close the browser
driver.quit()
