# The purpose of the code here is to retrieve a single piece of album artwork
# given the keys specified below and save the artwork to a folder as viewable file.

# Import Selenium, WebDriver, and Time (for sleep)
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib
import urllib.request
import time
from time import sleep
import random

PATH = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/chromedriver"

# This will eventually need to point to the actual music folder, but this will do for now.
# Make dynamic?
save_folder = "/Users/mgermaine93/Desktop/Album-Art"
seconds = [1, 2, 3, 4, 5]

# This creates the folder to store the image in
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

driver = webdriver.Chrome(PATH)

search_terms = ["John Coltrane Blue Train Album Cover",
                "The Silver Seas Chateau Revenge! Album Cover"]

count = 0

for term in search_terms:

    driver.get("https://www.google.com/imghp?hl=en&ogbl")
    search_bar = driver.find_element_by_name("q")
    search_bar.send_keys(term)
    search_bar.send_keys(Keys.RETURN)

    try:

        search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "islrg"))
        )

        images = search_results.find_elements_by_tag_name("img")

######## DIFFERENT CODE FROM ABOVE BEGINS HERE ########

        images[0].click()

        # Wait for the larger image to load
        new_search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "n3VNCb"))
        )

        large_image = new_search_results.find_element_by_class_name("n3VNCb")

        source = large_image.get_attribute('src')

        # Download and save the image
        urllib.urlretrieve(source, f"{save_folder}/{count}image.jpg")

######## DIFFERENT CODE FROM ABOVE ENDS HERE ########

        print("Artwork Saved")

        count += 1
        sleep(random.choice(seconds))

    except:

        print("Error")
        driver.quit()

driver.quit()
