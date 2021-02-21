# The purpose of the code here is to retrieve a single piece of album artwork
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import random
import urllib

# given the keys specified below and save the artwork to a folder as viewable file.

# Import Selenium, WebDriver, and Time (for sleep)
PATH = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/chromedriver"
save_folder = "/Users/mgermaine93/Desktop/Album-Art"
seconds = [1, 2, 3, 4, 5]

if not os.path.exists(save_folder):
    os.mkdir(save_folder)

driver = webdriver.Chrome(PATH)

search_terms = ["Ben Folds Songs for Silverman Album Cover",
                "The Silver Seas Chateau Revenge! Album Cover"]

count = 0

for term in search_terms:
    driver.get("https://www.google.com/imghp?hl=en&ogbl")
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys(term)
    search_bar.send_keys(Keys.RETURN)
    try:
        search_results = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            # (By.XPATH, '//a[@class="wXeWr islib nfEiy mM5pbd"]')))
            (By.ID, 'islrg')))
        images = search_results.find_elements(By.TAG_NAME, "img")
        images[0].click()
        # Wait for the larger image to load
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "n3VNCb")))
        large_image = driver.find_element(By.CLASS_NAME, "n3VNCb")
        source = large_image.get_attribute('src')
        # Download and save the image
        urllib.request.urlretrieve(source, f"{save_folder}/{count}image.jpg")

        # This will print if the above succeeds
        print("Artwork Saved")

        # Update count here
        count += 1

        # Good practice, keeps time between requests somewhat variadic
        time.sleep(random.choice(seconds))

    except:
        print("Error")
        driver.quit()

driver.quit()
