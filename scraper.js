// This file reads table data from fortnite.fandom.com listing page, because I'm not smart enough to
// datamine from the code.

var yoink = () => {
    const name = document.querySelector("[data-source='name']")?.innerText
    const artist = document.querySelector("[data-source='artist'] div a")?.innerText
    const year = document.querySelector("[data-source='year'] div")?.innerText
    const genre = document.querySelector("[data-source='genre'] div a")?.innerText
    const album = document.querySelector("[data-source='album'] div a")?.innerText
    const length = document.querySelector("[data-source='length'] div")?.innerText
    const key = document.querySelector("[data-source='key'] div a")?.innerText
    const bpm = document.querySelector("[data-source='bpm'] div")?.innerText
    const unlocked = document.querySelector("[data-source='unlocked'] div a")?.innerText
    const cost = document.querySelector("[data-source='cost'] div a")?.innerText
    const release = document.querySelector("[data-source='release'] div a")?.innerText
    const imageUrl = document.querySelector("[data-source='image'] div figure a img")?.src

    return {name, artist, year, genre, album, length, key, bpm, unlocked, cost, release, imageUrl}
}

console.log(yoink())