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
    export let image: string = ""

    const difficultyClasses = [
        "",
        "difficulty-1",
        "difficulty-2",
        "difficulty-3",
        "difficulty-4",
        "difficulty-5",
        "difficulty-6",
        "difficulty-7"
    ]
</script>

<article class="track">
    <header>
        <div class="title-group">
            <h4><span class="song-name">{name}</span> • <span class="artist">{artist}</span></h4>
        </div>
        <div class="difficulty-group">
            <div class="difficulty">
                <img src="/guitar.webp"/>
                <p class="{difficultyClasses[lead]}">{lead}</p>
            </div>
            <div class="difficulty">
                <img src="/bass.webp"/>
                <p class="{difficultyClasses[bass]}">{bass}</p>
            </div>
        </div>
    </header>
    <footer>
        <p style="opacity: 0.7;">{length} - {genre} - {bpm}<small>BPM</small></p>
        <div class="difficulty-group">
            <div class="difficulty">
                <img src="/drum.webp"/>
                <p class="{difficultyClasses[drums]}">{drums}</p>
            </div>
            <div class="difficulty">
                <img src="/microphone.webp"/>
                <p class="{difficultyClasses[vocals]}">{vocals}</p>
            </div>
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

    .difficulty-1 {

    }
</style>