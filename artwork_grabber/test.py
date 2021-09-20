from bs4 import BeautifulSoup
from selenium import webdriver

import os
from urllib.parse import urlparse

url = 'https://image.rakuten.co.jp/azu-kobe/cabinet/hair1/hb-30-pp1.jpg'

filename = os.path.basename(urlparse(url).path)
# change file extension to .png
filename_png = os.path.splitext(filename)[0] + '.png'

opts = webdriver.ChromeOptions()
opts.headless = True
driver = webdriver.Chrome(options=opts)

driver.get(url)

# Get the width and height of the image
soup = BeautifulSoup(driver.page_source, 'lxml')
width = soup.find('img')['width']
height = soup.find('img')['height']

# driver.set_window_size(int(width), int(height))
driver.set_window_size(width, height)
driver.save_screenshot(filename_png)
