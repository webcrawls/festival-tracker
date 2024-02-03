<script lang="ts">
    import '$lib/app.css'

    import {onMount} from "svelte";
    import Fuse from 'fuse.js'

    let searches: any[] = []
    let songs: any[] = []
    let fuse: Fuse<string> = null
    let search: string = ""

    $: searches = search === "" ? songs : fuse?.search(search).map(item => item.item)

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
    <input type="text" bind:value={search} placeholder="good 4 u"/>
    <table class="songs">
        {#if !songs}
            <h1>Loading songs...</h1>
        {/if}
        <thead>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">Artist</th>
                <th scope="col">Genre</th>
                <th scope="col">Length</th>
                <th scope="col">BPM</th>
            </tr>
        </thead>
        <tbody>
            {#each searches as song}
                <tr>
                    <td>{song.name}</td>
                    <td>{song.artist}</td>
                    <td>{song.genre}</td>
                    <td>{song.length}</td>
                    <td>{song.bpm}</td>
                </tr>
            {/each}
        </tbody>
    </table>
</main>

<style>

</style>
