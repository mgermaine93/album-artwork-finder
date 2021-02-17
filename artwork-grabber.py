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
import urllib.request
import time
from time import sleep

PATH = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/chromedriver"

# This will eventually need to point to the actual music folder, but this will do for now.
# Make dynamic?
save_folder = "/Users/mgermaine93/Desktop/DMB-Album-Art"

# This creates the folder to store the image in
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

driver = webdriver.Chrome(PATH)

# Goes to the given web page
driver.get("https://www.google.com/imghp?hl=en&ogbl")

# "q" is the name of the google search field input
search_bar = driver.find_element_by_name("q")

search_term = "Ben Folds Five The Sound of the Live of the Mind Album Cover"

# Input the search term(s)
# This will need to be dynamic, too
search_bar.send_keys(search_term)

# Returns the results (basically clicks "search"?)
search_bar.send_keys(Keys.RETURN)

# Wait 10 seconds for the images to load on the page before moving on to the next part of the script
try:
    # This will retrieve a list containing lots of images, but only once a "body" tag has loaded
    search_results = WebDriverWait(driver, 10).until(
        # Not sure if the ID will change, but it stays the same for at least three separate searches...
        EC.presence_of_element_located((By.ID, "islrg"))
    )
    # print(search_results.text)

    # Gets all of the images on the page (it should be a list)
    images = search_results.find_elements_by_tag_name("img")
    # print(images)

    # Just the first result should do for now.
    data_url = images[0].get_attribute('src')
    print(data_url)

    # (From SO post) Read the dataURL and decode it to bytes
    with urllib.request.urlopen(data_url) as response:
        data = response.read()
        with open(f"{save_folder}/image.jpg", mode="wb") as f:
            f.write(data)

    # This will print if the above succeeds
    print("Potato")

except:
    print("Booger")
    driver.quit()

# Closes the browser
driver.quit()

# https://stackoverflow.com/questions/6813704/how-to-download-an-image-using-selenium-any-version
# CSS selector styles:  style="height: 200px; margin-left: 2px; margin-right: 1px; margin-top: -10px;"
