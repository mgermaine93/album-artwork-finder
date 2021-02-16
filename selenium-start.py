# The purpose of the code here is to retrieve a single piece of album artwork
# given the keys specified below and save the artwork to a folder as viewable file.

# Import Selenium, WebDriver, and Time (for sleep)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib3
import time

PATH = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/chromedriver"

save_folder = "/Users/mgermaine93/Desktop/DMB-Album-Art"

# This creates the folder to store the image in
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

driver = webdriver.Chrome(PATH)

# Goes to the given web page
driver.get("https://www.google.com/imghp?hl=en&ogbl")

# "q" is the name of the google search field input
search_bar = driver.find_element_by_name("q")

# Input the search term(s)
search_bar.send_keys("Dave Matthews Band Crash Album Cover")

# Returns the results (basically clicks "search"?)
search_bar.send_keys(Keys.RETURN)

# Wait 10 seconds for the images to load on the page before moving on to the next part of the script
try:
    # This will retrieve a list containing lots of images, but only once a "body" tag has loaded
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Gets all of the images on the page (it should be a list)
    images = search_results.find_elements_by_tag_name("img")

    # Just the first result should do for now.
    image = images[0].get_attribute('src')

    if image != None:
        source = str(image)
        print(source)
        urllib3.request.urlretrieve(
            source, os.path.join(save_folder, 'dmb.jpg'))
    else:
        raise TypeError

except:
    driver.quit()

# Closes the browser
driver.quit()

# https://stackoverflow.com/questions/6813704/how-to-download-an-image-using-selenium-any-version
