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
import requests
from PIL import Image


PATH = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/chromedriver"

optionsforchrome = Options()
optionsforchrome.add_argument('--no-sandbox')
optionsforchrome.add_argument('--start-maximized')
optionsforchrome.add_argument('--disable-extensions')
optionsforchrome.add_argument('--disable-dev-shm-usage')
optionsforchrome.add_argument('--ignore-certificate-errors')
service = Service(ChromeDriverManager().install())


def get_album_artwork(search_term, save_folder):
    """
    Takes in a file path to a song and returns the file path to an image that this function has searched for, downloaded, and saved to a local location.

    :param file_path_to_song:  a file path to an .mp3 or .m4a file.
    :type file_path_to_song: `string`, required.

    :return:  an object of type string that represents the file path to the image that will serve as the album artwork to the song that was passed in.
    :rtype:  `string`.
    """

    # This will need to be update to be dynamic, I think
    # save_folder = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork"

    # creates the save_folder if it doesn't already exist
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)

    # uses previously found album artwork so as to prevent redundant scraping
    if os.path.exists(f"{save_folder}/{search_term}_new_artwork.jpeg"):
        return f"{save_folder}/{search_term}_new_artwork.jpeg"

    seconds = [3, 4, 5]

    # Thanks to https://python-forum.io/Thread-MaxRetryError-while-scraping-a-website-multiple-times
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.google.com/imghp?hl=en&ogbl")

    try:
        # This is the name of the google search bar field
        search_bar = driver.find_element(By.NAME, "q")
    except NoSuchElementException as e:
        print(f"No such element found:  {e}")

    # retrieves the google image search results using the phrase provided
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.RETURN)
    search_results = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.ID, 'islrg')))
    print("Initial image search worked.")

    # waits for the "Tools" button to load and clicks it
    tools_menu = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, ".PNyWAd.ZXJQ7c")))
    sleep(random.choice(seconds))
    tools_menu.click()
    print("Tool menu was found and clicked.")

    # clicks the "Size" dropdown (revealed by clicking the "Tools" button) once it is clickable
    size_menu = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, ".xFo9P.r9PaP")))
    sleep(random.choice(seconds))
    size_menu.click()
    print("Size option was found and clicked.")

    # selects the "Large" size option to filter large image sizes only.
    large_option = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[2]/div/span')))
    sleep(random.choice(seconds))
    large_option.click()
    print("Large option was found and clicked.")

    # clicks on the first large image
    large_image = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, '.rg_i.Q4LuWd')))
    sleep(random.choice(seconds))
    large_image.click()
    print("Large image was found and clicked.")

    # downloads and saves the large image to a local file
    large_image = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, '.n3VNCb')))
    sleep(random.choice(seconds))
    source = large_image.get_attribute("src")
    urllib.request.urlretrieve(
        source, f"{save_folder}/{search_term}_new_artwork.jpeg")

    # This will print if everything above works
    print(f"Artwork for {search_term} saved.")

    # Good practice, slows down the WebDriver
    sleep(random.choice(seconds))

    driver.quit()

    return f"{save_folder}/{search_term}_new_artwork.jpeg"


# get_album_artwork("Ben Folds Rockin the Suburbs Album Cover", "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork")
