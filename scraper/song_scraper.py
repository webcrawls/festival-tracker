# This script loads the URL dictionary from 'song_pages.json', visits each page, scrapes the song's information,
# and saves it in 'songs.json'.

import json
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with open("song_pages.json", "r") as f:
    song_links = json.load(f)

driver = webdriver.Firefox()
songs = []

for title, link in song_links.items():
    print("Scanning "+link)
    driver.get(link)
    time.sleep(3)

    artist_name = driver.find_element(By.CSS_SELECTOR, "[data-source='artist'] div a").text
    song_name = driver.find_element(By.CSS_SELECTOR, "[data-source='name']").text
    year = driver.find_element(By.CSS_SELECTOR, "[data-source='year'] div").text

    # Sometimes a genre isn't listed.
    try:
        genre = driver.find_element(By.CSS_SELECTOR, "[data-source='genre'] div a").text
    except Exception as e:
        print("Couldn't find a genre, 'N/A'")
        genre = "N/A"

    try:
        album = driver.find_element(By.CSS_SELECTOR, "[data-source='album'] div a").text
    except Exception as e:
        print("Couldn't find an album.")

        # Special case to handle Epic Games tracks.
        if artist_name == "Epic Games":
            print("Artist is Epic Games, album set to Epic Games")
            album = "Epic Games"
        else:
            album = "N/A"
    length = driver.find_element(By.CSS_SELECTOR, "[data-source='length'] div").text
    try:
        key = driver.find_element(By.CSS_SELECTOR, "[data-source='key'] div a").text
    except Exception as e:
        key = "N/A"
    bpm = driver.find_element(By.CSS_SELECTOR, "[data-source='bpm'] div").text
    try:
        unlocked = driver.find_element(By.CSS_SELECTOR, "[data-source='unlocked'] div a").text
    except Exception as e:
        unlocked = "N/A"
    try:
        cost = driver.find_element(By.CSS_SELECTOR, "[data-source='cost'] div").text
    except Exception as e:
        print("No cost.")
        cost = "N/A"
    release = driver.find_element(By.CSS_SELECTOR, "[data-source='release'] div").text
    image = driver.find_element(By.CSS_SELECTOR, "a.image.image-thumbnail img").get_attribute("src")

    song_obj = {"artist": artist_name,
                "name": song_name,
                "year": year,
                "genre": genre,
                "album": album,
                "length": length,
                "key": key,
                "bpm": bpm,
                "unlocked": unlocked,
                "cost": cost,
                "release": release,
                "image": image}

    print("Scanned "+title)

    songs.append(song_obj)

with open('songs.json', 'w+') as f:
    json.dump({"songs": songs}, f, indent=4)
