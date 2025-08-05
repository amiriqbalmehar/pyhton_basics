from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the GeckoDriver service
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # Navigate to the Google Play Store's New Apps section
    driver.get('https://play.google.com/store/apps')

    # Wait for the page to load and the apps to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'WHE7ib'))
    )

    # Find all apps listed on the page
    apps = driver.find_elements(By.CLASS_NAME, 'WHE7ib')

    for app in apps:
        # Click on each app to navigate to its detail page
        app.click()

        # Wait for the app detail page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'AHFaub'))
        )

        # Scraping required details
        try:
            app_name = driver.find_element(By.CLASS_NAME, 'AHFaub').text
            developer_name = driver.find_element(By.CLASS_NAME, 'hrTbp R8zArc').text
            rating = driver.find_element(By.CLASS_NAME, 'BHMmbe').text
            downloads = driver.find_element(By.CLASS_NAME, 'BgcNfc').text
            release_date = driver.find_element(By.CLASS_NAME, 'xKpxId').text
            description = driver.find_element(By.CLASS_NAME, 'DWPxHb').text
            category = driver.find_element(By.CLASS_NAME, 'T32cc').text

            # Print the details
            print(f"App Name: {app_name}")
            print(f"Developer Name: {developer_name}")
            print(f"Rating: {rating}")
            print(f"Number of Downloads: {downloads}")
            print(f"Release Date: {release_date}")
            print(f"Description: {description}")
            print(f"Category: {category}")
            print("-" * 50)

        except Exception as e:
            print(f"Could not retrieve details for {app_name}: {e}")

        # Go back to the previous page
        driver.back()

        # Wait for the main page to load again
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'WHE7ib'))
        )

finally:
    driver.quit()
