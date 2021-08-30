from selenium.common.exceptions import (
    NoSuchElementException,
    NoSuchAttributeException,
    InvalidSelectorException
)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
import random
import urllib
from mutagen.mp4 import MP4, MP4Cover
from mutagen import File
from mutagen.id3 import ID3, APIC, error
from mutagen.mp3 import MP3
from mutagen.m4a import M4ACover
from tinytag import TinyTag
from pathlib import Path


class Song:
    def __init__(self, file_path_to_song):
        self.file_path_to_song = file_path_to_song

    def print_file_path(self):
        print(self.file_path_to_song)

    def get_album(self):
        return TinyTag.get(self.file_path_to_song).album
        # print(TinyTag.get(self.file_path_to_song).album)

    def get_album_artist(self):
        return TinyTag.get(self.file_path_to_song).albumartist

    def get_artist(self):
        return TinyTag.get(self.file_path_to_song).artist

    def get_audio_offset(self):
        return TinyTag.get(self.file_path_to_song).audio_offset

    def get_bitrate(self):
        return TinyTag.get(self.file_path_to_song).bitrate

    def get_comment(self):
        return TinyTag.get(self.file_path_to_song).comment

    def get_composer(self):
        return TinyTag.get(self.file_path_to_song).composer

    def get_disc(self):
        return TinyTag.get(self.file_path_to_song).disc

    def get_disc_total(self):
        return TinyTag.get(self.file_path_to_song).disc_total

    def get_disc_total(self):
        return TinyTag.get(self.file_path_to_song).disc_total

    def get_duration(self):
        return TinyTag.get(self.file_path_to_song).duration

    def get_filesize(self):
        return TinyTag.get(self.file_path_to_song).filesize

    def get_genre(self):
        return TinyTag.get(self.file_path_to_song).genre

    def get_samplerate(self):
        return TinyTag.get(self.file_path_to_song).samplerate

    def get_title(self):
        return TinyTag.get(self.file_path_to_song).title

    def get_track(self):
        return TinyTag.get(self.file_path_to_song).track

    def get_track_total(self):
        return TinyTag.get(self.file_path_to_song).track_total

    def get_year(self):
        return TinyTag.get(self.file_path_to_song).year


def get_search_term(song):
    album = Song.get_album(song)
    artist = Song.get_artist(song)
    term = f"{artist} {album} album cover"
    print(f"Output of get_search_term() function: {term}")
    return term


def detect_album_artwork(song):

    file_type = Path(song.file_path_to_song).suffix.lower()

    if file_type == ".m4a":
        try:
            track = MP4(song)
            tags = track.tags
            tags['covr']
            return True
        except KeyError:
            print("M4A track needs album artwork")
            return False

    elif file_type == ".mp3":
        try:
            mp3 = MP3(song, ID3=ID3)
            tags = mp3.tags
            tags['covr']
            return True
        except KeyError:
            print("MP3 track needs album artwork")
            return False

    else:
        print("Filename name is not M4A nor MP3")
        return False


def embed_album_artwork(song, album_art):

    file_type = Path(song.file_path_to_song).suffix.lower()

    print(file_type)
    if file_type == ".m4a":
        track = MP4(song.file_path_to_song)

        # Thanks to: https://stackoverflow.com/questions/37897801/embedding-album-cover-in-mp4-file-using-mutagen
        with open(album_art, "rb") as f:
            track.tags["covr"] = [
                MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_JPEG)
            ]
            track.save()
            print("artwork saved")

    elif file_type == ".mp3":
        # Thanks to https://stackoverflow.com/questions/409949/how-do-you-embed-album-art-into-an-mp3-using-python
        mp3 = MP3(song.file_path_to_song, ID3=ID3)
        mp3.tags.add(
            APIC(
                encoding=3,  # 3 is for utf-8
                mime='image/jpg',  # image/jpeg or image/png
                type=3,  # 3 is for the cover image
                desc=u'Cover',
                data=open(album_art, "rb").read()
            )
        )
        print("Artwork added")
        mp3.save()
    else:
        print("Filename name is not M4A nor MP3")


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
        print("No such element found!")

    try:
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.RETURN)
        search_results = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.ID, 'islrg')))
    except InvalidSelectorException:
        print("XPath selector is either incorrect or syntactically invalid!")

    try:
        images = search_results.find_elements(By.TAG_NAME, "img")
    except NoSuchElementException:
        print("No images found!")

    # Just the first image will do.
    images[0].click()

    try:
        # Wait for the larger image to load
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "n3VNCb")))
        large_image = driver.find_element(By.CLASS_NAME, "n3VNCb")
    except NoSuchElementException:
        print("An element with the provided element name could not be found!")

    try:
        source = large_image.get_attribute('src')
    except NoSuchAttributeException:
        print("An element with the provided attribute could not be found!")

    # Download and save the image
    # urllib.request.urlretrieve(source, f"{save_folder}/artwork.jpg")

    sleep(2)
    cover = driver.find_element_by_class_name('n3VNCb')

    # thanks to https://www.geeksforgeeks.org/screenshot-element-method-selenium-python/
    # and https://stackoverflow.com/questions/3422262/how-can-i-take-a-screenshot-with-selenium-webdriver
    cover.screenshot(f"{save_folder}/artwork.png")

    # This will print if everything above works
    print(f"Artwork for {search_term} saved.")
    count += 1

    # Good practice, slows down the WebDriver
    sleep(random.choice(seconds))

    driver.quit()


song = Song('/Users/mgermaine93/Desktop/02 Shoot To Thrill.m4a')
song.print_file_path()
get_search_term(song)
detect_album_artwork(song.file_path_to_song)
file_type = Path(song.file_path_to_song).suffix
print(file_type)
get_album_artwork(get_search_term(song),
                  "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork")
embed_album_artwork(
    song, "/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork/artwork.png")
