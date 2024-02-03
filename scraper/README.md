# Festival Tracker Scraper

This project serves to scrape fortnite.fandom.com for:

- a list of all Jam Tracks, along with their respective wiki URLs
- song information for each Jam Track, i.e. title, difficulty, etc.

Sadly, song difficulties are not listed on the site, so these will still need to be manually entered.
However, this tool gets us a good way there, which is good enough for me :)

## Usage

Run `page_scraper.py` to create a `song_pages.json` file containing a dictionary mapping song titles to their wiki page URL.

Next, run `song_scraper.py` to create a `songs.json` file containing each song's information. This requires `song_pages.json` to be present.