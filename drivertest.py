from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Provide the correct path to the chromedriver executable
chromedriver_path = '"C:\Windows\chromedriver-win64\chromedriver.exe"' #Update this path where your chromedriver is stored as i have stored at the path provided

# Create a Service object
service = Service(chromedriver_path)

# Use the Service object in the WebDriver
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
