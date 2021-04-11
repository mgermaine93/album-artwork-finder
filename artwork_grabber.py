"""
Purpose of this file:
- Given a search term, e.g. "album_here artist_here album cover", go out and find the album artwork
- Save the retrieved artwork to a hardcoded folder for now.
"""

import urllib
import random
import os
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException, InvalidSelectorException

PATH = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/chromedriver"

# This will need to be update to be dynamic, I think
save_folder = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork"

if not os.path.exists(save_folder):
    os.mkdir(save_folder)

optionsforchrome = Options()
optionsforchrome.add_argument('--no-sandbox')
optionsforchrome.add_argument('--start-maximized')
optionsforchrome.add_argument('--disable-extensions')
optionsforchrome.add_argument('--disable-dev-shm-usage')
optionsforchrome.add_argument('--ignore-certificate-errors')
service = Service(ChromeDriverManager().install())


def get_album_artwork(search_term, save_folder):

    seconds = [3, 4, 5]
    count = 0

    # Thanks to https://python-forum.io/Thread-MaxRetryError-while-scraping-a-website-multiple-times
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.google.com/imghp?hl=en&ogbl")

    try:
        # This is the name of the google search bar field
        search_bar = driver.find_element(By.NAME, "q")
    except NoSuchElementException:
        raise NoSuchElementException("No such element found!")

    try:
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.RETURN)
        search_results = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, '//a[@class="wXeWr islib nfEiy mM5pbd"]')))
    except InvalidSelectorException:
        raise InvalidSelectorException(
            "XPath selector is either incorrect or syntactically invalid!")

    try:
        images = search_results.find_elements(By.TAG_NAME, "img")
    except NoSuchElementException:
        raise NoSuchElementException("No images found!")

    # Just the first image will do.
    images[0].click()

    try:
        # Wait for the larger image to load
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "n3VNCb")))
        large_image = driver.find_element(By.CLASS_NAME, "n3VNCb")
    except NoSuchElementException:
        raise NoSuchElementException(
            "An element with the provided element name could not be found!")

    try:
        source = large_image.get_attribute('src')
    except NoSuchAttributeException:
        raise NoSuchAttributeException(
            "An element with the provided attribute could not be found!")

    # Download and save the image
    # urllib.request.urlretrieve(source, f"{save_folder}/artwork.jpg")

    sleep(2)
    cover = driver.find_element_by_xpath(
        '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img')

    # thanks to https://www.geeksforgeeks.org/screenshot-element-method-selenium-python/
    # and https://stackoverflow.com/questions/3422262/how-can-i-take-a-screenshot-with-selenium-webdriver
    cover.screenshot(f"{save_folder}/artwork.png")

    # This will print if everything above works
    print(f"Artwork for {search_term} saved.")
    count += 1

    # Good practice, slows down the WebDriver
    sleep(random.choice(seconds))

    driver.quit()


get_album_artwork("Ben Folds Rockin the Suburbs Album Cover",
                  "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork")
