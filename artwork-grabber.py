import urllib
import random
import os
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

PATH = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/chromedriver"
save_folder = "/Users/mgermaine93/Desktop/Album-Art"

driver = webdriver.Chrome(PATH)

seconds = [1, 2, 3, 4, 5]

if not os.path.exists(save_folder):
    os.mkdir(save_folder)

optionsforchrome = Options()
optionsforchrome.add_argument('--no-sandbox')
optionsforchrome.add_argument('--start-maximized')
optionsforchrome.add_argument('--disable-extensions')
optionsforchrome.add_argument('--disable-dev-shm-usage')
optionsforchrome.add_argument('--ignore-certificate-errors')
service = Service(ChromeDriverManager().install())

search_terms = ["John Coltrane Blue Train Album Cover",
                "The Silver Seas Chateau Revenge! Album Cover"]

count = 0

for term in search_terms:
    driver.get("https://www.google.com/imghp?hl=en&ogbl")

    # This is the name of the google search bar field
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys(term)
    search_bar.send_keys(Keys.RETURN)
    try:
        search_results = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '//a[@class="wXeWr islib nfEiy mM5pbd"]')))
        images = search_results.find_elements(By.TAG_NAME, "img")

        # Just the first image will do.
        images[0].click()

        # Wait for the larger image to load
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "n3VNCb")))
        large_image = driver.find_element(By.CLASS_NAME, "n3VNCb")
        source = large_image.get_attribute('src')

        # Download and save the image
        urllib.request.urlretrieve(source, f"{save_folder}/{count}image.jpg")

        # This will print if everything above works
        print("Artwork Saved")
        count += 1

        # Good practice, slows down the WebDriver
        sleep(random.choice(seconds))

    except:
        print("Error")
        driver.quit()

driver.quit()