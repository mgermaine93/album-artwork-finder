# Import Selenium, WebDriver, and Time (for sleep)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/chromedriver"

driver = webdriver.Chrome(PATH)

# Goes to the given web page
driver.get("https://www.google.com/imghp?hl=en&ogbl")

# "q" is the name of the google search field input
search_bar = driver.find_element_by_name("q")

# Input the search term(s)
search_bar.send_keys("Dave Matthews Band Crash Album Cover")

# Returns the results
search_bar.send_keys(Keys.RETURN)

# Wait 10 seconds for the images to load on the page before moving on to the next part of the script
try:
    # This will retrieve a list containing lots of images
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    # We just want the first result for now... implement this soon.
    print(search_results.text)
    # for image in images:
    #     src = image.getAttribute('src')
    #     print(src.text)

    # album_artwork = search_results[0].getAttribute("src")
    # print(album_artwork)
    # Need to figure out how to retrieve the "src" of the image
except:
    driver.quit()

# Closes the browser
driver.quit()

# https://stackoverflow.com/questions/6813704/how-to-download-an-image-using-selenium-any-version
