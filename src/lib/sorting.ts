export const sortByLead = (a, b) => {
    const diffA = a.difficulties?.lead ?? 0
    const diffB = b.difficulties?.lead ?? 0
    return diffB - diffA
}

export const vocals = (a, b) => {
    const diffA = a.difficulties?.vocals ?? 0
    const diffB = b.difficulties?.vocals ?? 0
    return diffB - diffA
}
export const drums = (a, b) => {
    const diffA = a.difficulties?.drums ?? 0
    const diffB = b.difficulties?.drums ?? 0
    return diffB - diffA
}
export const lead = (a, b) => {
    const diffA = a.difficulties?.lead ?? 0
    const diffB = b.difficulties?.lead ?? 0
    return diffB - diffA
}
export const bass = (a, b) => {
    const diffA = a.difficulties?.bass ?? 0
    const diffB = b.difficulties?.bass ?? 0
    return diffB - diffA
}
export const bpm = (a, b) => {
    const aBpm = parseInt(a.bpm)
    const bBpm = parseInt(b.bpm)
    return bBpm - aBpm
}