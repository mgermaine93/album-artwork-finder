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
import requests
from PIL import Image


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
    urllib.request.urlretrieve(source, f"{save_folder}/new_artwork.png")

    # This will print if everything above works
    print(f"Artwork for {search_term} saved.")
    count += 1

    # Good practice, slows down the WebDriver
    sleep(random.choice(seconds))

    driver.quit()


get_album_artwork("Ben Folds Rockin the Suburbs Album Cover",
                  "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork")

# # large_image.click()
# # print("Large image was found and clicked.")

# # try:
# #     # Wait for the larger image to load
# #     WebDriverWait(driver, 10).until(
# #         ec.presence_of_element_located((By.CLASS_NAME, "n3VNCb")))
# #     large_image = driver.find_element(By.CLASS_NAME, "n3VNCb")
# # except NoSuchElementException:
# #     print("An element with the provided element name could not be found!")

# # try:
# #     source = large_image.get_attribute("src")
# #     urllib.request.urlretrieve(source, "captcha2.png")

# # except NoSuchAttributeException:
# #     print("An element with the provided attribute could not be found!")

# # WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@class='.PNyWAd.ZXJQ7c' and @jsname='I4bIT']")))

# # # By.XPATH, "// *[@class = 'ng-binding ng-scope'
# # tools_button = driver.find_element(
# #     (By.XPATH, "//*[@class='.PNyWAd ZXJQ7c' and @jsname='I4bIT']"))
# # tools_button.click()
# WebDriverWait(driver, 10).until(
#     ec.presence_of_element_located((By.CSS_SELECTOR, ".xFo9P r9PaP")))
# size_button = driver.find_element((By.CSS_SELECTOR, ".xFo9P r9PaP"))
# size_button.click()
# WebDriverWait(driver, 10).until(
#     ec.presence_of_element_located((By.CSS_SELECTOR, ".igM9Le")))
# large_option = driver.find_element((By.CSS_SELECTOR, ".igM9LeP"))
# large_option.click()
# WebDriverWait(driver, 10).until(
#      ec.presence_of_element_located((By.TAG_NAME, "img")))
#  images = search_results.find_elements((By.TAG_NAME, "img"))

#   # Just the first image will do.
#   images[0].click()

#    try:
#         # Wait for the larger image to load
#         WebDriverWait(driver, 10).until(
#             ec.presence_of_element_located((By.CLASS_NAME, "n3VNCb")))
#         large_image = driver.find_element(By.CLASS_NAME, "n3VNCb")
#     except NoSuchElementException:
#         print("An element with the provided element name could not be found!")

#     try:
#         source = large_image.get_attribute("src")
#         urllib.request.urlretrieve(source, "captcha.png")

#         # response = requests.get(source)
#         # if response.status_code == 200:
#         #     with open(f"{save_folder}/new_artwork.jpg", "wb") as file:
#         #         file.write(response.content)
#         # else:
#         #     print("Booger")
#         # source = large_image.get_attribute('src')
#     except NoSuchAttributeException:
#         print("An element with the provided attribute could not be found!")

#     # # This will print if everything above works
#     # print(f"Artwork for {search_term} saved.")
#     # count += 1

#     # # Good practice, slows down the WebDriver
#     # sleep(random.choice(seconds))

#     # driver.quit()

#     # Download and save the image
#     # urllib.request.urlretrieve(source, f"{save_folder}/artwork.jpg")

#     # sleep(2)
#     # # cover = driver.find_element_by_class_name('n3VNCb')
#     # cover = Image.open(r"captcha.png")
#     # resized_cover = cover.resize(500, 500)
#     # resized_cover.save('test-image-cover.png')
#     # thanks to https://www.geeksforgeeks.org/screenshot-element-method-selenium-python/
#     # and https://stackoverflow.com/questions/3422262/how-can-i-take-a-screenshot-with-selenium-webdriver
#     # cover.screenshot(f"{save_folder}/artwork.png")


# # PATH = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/chromedriver"

# # # This will need to be update to be dynamic, I think
# # save_folder = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork"

# # if not os.path.exists(save_folder):
# #     os.mkdir(save_folder)

# # optionsforchrome = Options()
# # optionsforchrome.add_argument('--no-sandbox')
# # optionsforchrome.add_argument('--start-maximized')
# # optionsforchrome.add_argument('--disable-extensions')
# # optionsforchrome.add_argument('--disable-dev-shm-usage')
# # optionsforchrome.add_argument('--ignore-certificate-errors')
# # service = Service(ChromeDriverManager().install())


# # def get_album_artwork(search_term, save_folder):

# #     seconds = [3, 4, 5]
# #     count = 0

# #     # Thanks to https://python-forum.io/Thread-MaxRetryError-while-scraping-a-website-multiple-times
# #     driver = webdriver.Chrome(PATH)
# #     driver.get("https://www.google.com/imghp?hl=en&ogbl")

# #     try:
# #         # This is the name of the google search bar field
# #         search_bar = driver.find_element(By.NAME, "q")
# #     except NoSuchElementException:
# #         print("No such element found!")

# #     try:
# #         search_bar.send_keys(search_term)
# #         search_bar.send_keys(Keys.RETURN)
# #         search_results = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
# #             (By.ID, 'islrg')))
# #     except InvalidSelectorException:
# #         print("XPath selector is either incorrect or syntactically invalid!")

# #     try:
# #         images = search_results.find_elements(By.TAG_NAME, "img")
# #     except NoSuchElementException:
# #         print("No images found!")

# #     # Just the first image will do.
# #     images[0].click()

# #     try:
# #         # Wait for the larger image to load
# #         WebDriverWait(driver, 10).until(
# #             ec.presence_of_element_located((By.CLASS_NAME, "n3VNCb")))
# #         large_image = driver.find_element(By.CLASS_NAME, "n3VNCb")
# #     except NoSuchElementException:
# #         print("An element with the provided element name could not be found!")

# #     try:
# #         source = large_image.get_attribute('src')
# #     except NoSuchAttributeException:
# #         print("An element with the provided attribute could not be found!")

# #     # Download and save the image
# #     # urllib.request.urlretrieve(source, f"{save_folder}/artwork.jpg")

# #     sleep(2)
# #     cover = driver.find_element_by_class_name('n3VNCb')

# #     # thanks to https://www.geeksforgeeks.org/screenshot-element-method-selenium-python/
# #     # and https://stackoverflow.com/questions/3422262/how-can-i-take-a-screenshot-with-selenium-webdriver

# #     # NEED TO FIGURE OUT HOW TO GET RID OF THE IMAGE'S OVERLAYING X'S, etc.
# #     cover.screenshot(f"{save_folder}/artwork.png")

# #     # This will print if everything above works
# #     print(f"Artwork for {search_term} saved.")
# #     count += 1

# #     # Good practice, slows down the WebDriver
# #     sleep(random.choice(seconds))

# #     driver.quit()


# # song = Song('/Users/mgermaine93/Desktop/02 Shoot To Thrill.m4a')
# # song.print_file_path()
# # get_search_term(song)
# # detect_album_artwork(song.file_path_to_song)
# # file_type = Path(song.file_path_to_song).suffix
# # print(file_type)
# # get_album_artwork(get_search_term(song),
# #                   "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork")
# # embed_album_artwork(
# #     song, "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork/artwork.png")


# # this might be helpful:  https://levelup.gitconnected.com/how-to-download-google-images-using-python-2021-82e69c637d59
