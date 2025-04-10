import os
from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Set up the Mozilla(Gecko) driver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


# Function to find image URLs
def get_image_urls(driver):
    image_tags = driver.find_elements(By.XPATH, "//a[@class='link--WHWzm']//img")
    return [img.get_attribute('src') for img in image_tags if 'jpg' in img.get_attribute('src')]

# Function to visit a page and collect image URLs
def collect_images_from_page(page_number):
    URL = f'https://pixabay.com/images/search/ai%20generated/?pagi={page_number}'
    driver.get(URL)
    time.sleep(5)  # Allow some time for the page to load
    return get_image_urls(driver)

# Collect image URLs from multiple pages
num_pages = 60
all_image_urls = []

for page_number in range(1, num_pages + 1):
    print(f"Collecting images from page {page_number}")
    image_urls = collect_images_from_page(page_number)
    all_image_urls.extend(image_urls)
    print(f"Total images collected so far: {len(all_image_urls)}")

# Create a directory to store the images
directory = 'downloaded_images'
if not os.path.exists(directory):
    os.makedirs(directory)

# Download the images and save them in the created folder
for index, url in enumerate(all_image_urls):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        image_path = os.path.join(directory, f'img0-{index+1}.jpg')
        with open(image_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
        print(f"Downloaded {image_path}")
    else:
        print(f"Failed to download {url}")

# Close the browser
driver.close()
