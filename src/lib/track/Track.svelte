<script lang="ts">
    export let name: string = "Unknown Song"
    export let artist: string = "Unknown Artist"
    export let length: string = "0:00"
    export let genre: string = "N/A"
    export let bpm: string = ""

    export let lead: number = 0
    export let drums: number = 0
    export let vocals: number = 0
    export let bass: number = 0

</script>

<article class="track">
    <header>
        <div class="title-group">
            <h4><span class="song-name">{name}</span> • <span class="artist">{artist}</span></h4>
        </div>
        <div class="difficulty-group">
            <img src="/guitar.webp"/>
            <p>{lead}</p>
            <img src="/bass.webp"/>
            <p>{bass}</p>
        </div>
    </header>
    <footer>
        <p>{length} - {genre} - {bpm}<small>BPM</small></p>
        <div class="difficulty-group">
            <img src="/drum.webp"/>
            <p>{drums}</p>
            <img src="/microphone.webp"/>
            <p>{vocals}</p>
        </div>
    </footer>
</article>

<style>
    article {
        border: 1px solid gray;
        border-radius: 3px;
        padding: 0.3rem;
    }

    header {
        margin: 0;
    }
</style>