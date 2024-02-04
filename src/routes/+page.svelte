<script lang="ts">
    import '$lib/app.css'

    import {onMount} from "svelte";
    import Fuse from 'fuse.js'

    let searches: any[] = []
    let songs: any[] = []
    let fuse: Fuse<string> = null
    let search: string = ""
    let sortingMethod: string = "release"
    $: sortingFn = sortingMethods[sortingMethod]

    $: searches = search === "" ? songs : fuse?.search(search).map(item => item.item)
    $: searches = searches.sort(sortingFn)

    const sortingMethods = {
        'lead': (a, b) => {
            const diffA = a.difficulties?.lead ?? 0
            const diffB = b.difficulties?.lead ?? 0
            return diffB - diffA
        },
        'vocals': (a, b) => {
            const diffA = a.difficulties?.vocals ?? 0
            const diffB = b.difficulties?.vocals ?? 0
            return diffB - diffA
        },
        'drums': (a, b) => {
            const diffA = a.difficulties?.drums ?? 0
            const diffB = b.difficulties?.drums ?? 0
            return diffB - diffA
        },
        'bass': (a, b) => {
            const diffA = a.difficulties?.lead ?? 0
            const diffB = b.difficulties?.lead ?? 0
            return diffB - diffA
        },
        'bpm': (a, b) => {
            const aBpm =  parseInt(a.bpm)
            const bBpm = parseInt(b.bpm)
            return bBpm- aBpm
        }
    }

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
    <section>
        <h3>Sort By</h3>
        <select bind:value={sortingMethod}>
            <option value="lead">Lead</option>
            <option value="drums">Drums</option>
            <option value="vocals">Vocals</option>
            <option value="bass">Bass</option>
        </select>
    </section>
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
                <th on:click={() => sortingMethod = 'lead'} scope="col" class="instrument">Lead</th>
                <th on:click={() => sortingMethod = 'vocals'} scope="col" class="instrument">Vocals</th>
                <th on:click={() => sortingMethod = 'drums'} scope="col" class="instrument">Drums</th>
                <th on:click={() => sortingMethod = 'bass'} scope="col" class="instrument">Bass</th>
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
                    <td>{song?.difficulties?.lead ?? 'N/A'}</td>
                    <td>{song?.difficulties?.vocals ?? 'N/A'}</td>
                    <td>{song?.difficulties?.drums ?? 'N/A'}</td>
                    <td>{song?.difficulties?.bass ?? 'N/A'}</td>
                </tr>
            {/each}
        </tbody>
    </table>
    <p style="font-style: italic; opacity: 0.7">hey. there may be some inconsistencies or incorrect information here. if you notice something wrong, leave an issue or suggest a change on GitHub!</p>
</main>

<style>

</style>
