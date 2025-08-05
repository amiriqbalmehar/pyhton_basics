from selenium import webdriver

# Create a new Firefox session
driver = webdriver.Firefox()

# Open a website
driver.get("https://www.python.org")

# Print the page title
print(driver.title)

# Close the browser
driver.quit()
