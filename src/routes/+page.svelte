<script lang="ts">
    import '$lib/app.css'

    import {onMount} from "svelte";
    import Fuse from 'fuse.js'
    import {bass, bpm, drums, lead, vocals} from "$lib/sorting";
    import Track from "$lib/track/Track.svelte";

    let searches: any[] = []
    let songs: any[] = []
    let fuse: Fuse<string> = null
    let search: string = ""
    let sortingMethod: (a, b) => number = (a, b) => 0

    $: searches = search === "" ? songs : fuse?.search(search).map(item => item.item)
    $: searches = searches.sort(sortingMethod)

    onMount(async () => {
        const res = await fetch("/songs.json")
        const json = await res.json()
        songs = json['songs']
        setupSearch()
    })

    const setupSearch = () => {
        fuse = new Fuse<string>(songs, {
            keys: [
                "name",
                "artist",
            ],
            minMatchCharLength: 2
        })
    }
</script>

<main>
    <header>
        <h1>FESTIVAL TRACKER</h1>
        <p>Explore, sort, and demo songs from the Fortnite Festival Jam Stage.</p>
    </header>
    <hr/>
    <section>
        <h1>Tracks</h1>
        <div class="option-group">
            <div class="option">
                <p>sorting by</p>
                <select bind:value={sortingMethod}>
                    <option value="{(a, b) => 0}">Duration</option>
                    <option value={bpm}>BPM</option>
                    <option value={lead}>Lead</option>
                    <option value={drums}>Drums</option>
                    <option value={vocals}>Vocals</option>
                    <option value={bass}>Bass</option>
                </select>
            </div>
            <input type="text" bind:value={search} placeholder="good 4 u"/>
        </div>
        <div class="track-group">
        {#each searches as song}
            <Track name="{song.name}"
                   artist="{song.artist}"
                   length="{song.length}"
                   genre="{song?.genre}"
                   lead="{song?.difficulties?.lead}"
                   drums="{song?.difficulties?.drums}"
                   vocals="{song?.difficulties?.vocals}"
                   bass="{song?.difficulties?.bass}" />
        {/each}
        </div>
    </section>
    <p style="font-style: italic; opacity: 0.7">hey. there may be some inconsistencies or incorrect information here. if you notice something wrong, leave an issue or <a href="https://github.com/webcrawls/festival-tracker">suggest a change on GitHub!</a></p>
</main>
