# This script visits the Fortnite Fandom Jam Tracks page, finds all jam track name & wiki URLs,
# and saves them to 'song_pages.json'.

import json
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

jam_tracks_list_url = "https://fortnite.fandom.com/wiki/Jam_Tracks"

driver = webdriver.Firefox()
driver.get(jam_tracks_list_url)

time.sleep(2)

# 1. Select 'I'm an adult' popup if present
button_element = driver.find_element(By.CSS_SELECTOR, "#adult")
if button_element:
    button_element.click()

# 3. Scroll to bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 2. Wait a bit
time.sleep(3)

# 4. Find all song items in the table
elements = driver.find_elements(By.CSS_SELECTOR, "tr td p b a")

songs = {}

# Manual special cases to ignore certain links that may pop up in our selector.
# This may need to be adjusted over time (unless someone smarter comes along and thinks up a better solution :p)
ignored_text = ["Battle Pass", "Festival Pass", "V-Bucks", "Winterfest 2023"]
ignored_links = ["https://fortnite.fandom.com/wiki/Chapter_5:_Season_1#Battle_Pass",
                 "https://fortnite.fandom.com/wiki/Festival_Pass#Season_1",
                 "https://fortnite.fandom.com/wiki/Winterfest_2023",
                 "https://fortnite.fandom.com/wiki/V-Bucks"]

for elem in elements:
    for text in ignored_text:
        if text in elem.text:
            continue

    url = elem.get_attribute("href")

    if url in ignored_links:
        continue

    title = elem.get_attribute("title")

    songs[title] = url

driver.close()

os.remove('song_pages.json')

with open('song_pages.json', 'w+') as f:
    json.dump(songs, f, indent=4)
