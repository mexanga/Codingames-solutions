
 String.prototype.replaceAt = function(index, replacement) {
    return (index >= this.length) ? this.valueOf() : (this.substring(0, index) + replacement + this.substring(index + 1));
}

const [W,H,T1,T2,T3] = readline().split(' ').map(entry => parseInt(entry))

const times = [T1,T2,T3]

let asteroids = {}

let matches

const pattern = /(\w{1})/

for (let i = 0; i < H; i++) {
    let cursor = -1;
    for (let entry of readline().split(' ')) {
        cursor++
        while (pattern.test(entry)) {
            matches = entry.match(pattern)
            if (!asteroids.hasOwnProperty(matches[0])) {
               asteroids[matches[0]] = {}
            }
            asteroids[matches[0]][times[cursor]] = [i,matches.index]
            entry = entry.replaceAt(matches.index, '.')
        }
    }
}

for (let letter in asteroids) {
    try {
        let diff = [
            (asteroids[letter][times[1]][0] - asteroids[letter][times[0]][0]),
            (asteroids[letter][times[1]][1] - asteroids[letter][times[0]][1]),
        ]
        let ratioDiffBis = times[1] - times[0]
        let ratioDiff = times[2] - times[1]
        asteroids[letter][times[2]] = [
            asteroids[letter][times[1]][0] + (diff[0] * ratioDiff)/ratioDiffBis,
            asteroids[letter][times[1]][1] + (diff[1] * ratioDiff)/ratioDiffBis
        ]
        for (let time in asteroids[letter]) {
            asteroids[letter][time] = asteroids[letter][time].map(entry => Math.floor(entry))
        }
    }
    catch(e) { continue; }
}

for (let i = 0; i < H; i++) {
    let row = (new Array(W)).fill('.').join('')
    for (let [letter,positions] of Object.entries(asteroids).sort().reverse()) {
        if (i === positions[times[2]][0] && W > positions[times[2]][1] && 0 <= positions[times[2]][1]) {
            row = row.replaceAt(positions[times[2]][1], letter)
        }
    }
    console.log(row)
}
