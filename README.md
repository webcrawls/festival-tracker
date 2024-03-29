# Festival Tracker

**Festival Tracker** is a data visualization tool created to explore the Fortnite Festival track list. It provides a
sortable list of all tracks in the game.

Built with svelte and fuse.js.

## Motivation

I really like Fortnite Festival, I think it has potential to be one of the best rhythm games, but it still leaves a bit to be desired. One pain point is the in-game UI makes it difficult to view and sort
tracks by difficulty, which is something I believe is very important in a rhythm game.

I hope this project can act as a stop-gap solution while the Festival team works on updates and improvements. And I hope
to learn and improve on my knowledge of some technologies for myself.

## Technologies

- Svelte for the front-end
- fuse.js for fussy searching
- Selenium for scraping fortnite.fandom.com.

## TODO

- Cleaner styling
- Explore grabbing song data from Fortnite APIs directly
- Add 'play song on <spotify/apple/ytm>' buttons

## Caveats

* Not all tracks have genres yet.
* Sorting by length hasn't been added.
* Song names are in full-caps, I don't have a decent fix aside from manually editing each. Some day!