
 String.prototype.replaceAt = function(index, replacement) {
    return (index >= this.length) ? this.valueOf() : (this.substring(0, index) + replacement + this.substring(index + 1));
}

// Entrées récupérables
const [W,H,T1,T2,T3] = readline().split(' ').map(entry => parseInt(entry))

const times = [T1,T2,T3]

// Chaque asteroid aura pour une lettre donnée comme clé, les positions sur les différents temps.
let asteroids = {}

// Pattern permettant de récupérer une lettre
const pattern = /(\w{1})/

// On recupere la position des asteroids en t1 et t2
for (let i = 0; i < H; i++) {
    // Le curseur est utilisé pour manipuler les temps
    let cursor = -1;
    // Pour chaque ligne, (les temps sont traités en même temps)
    for (let entry of readline().split(' ')) {
        cursor++
        // On recupere les lettres sur la ligne
        // La boucle se termine une fois qu'il n'y a plus de lettres à traitées.
        while (pattern.test(entry)) {
            let matches = entry.match(pattern)
            // Si l'asteroid n'a pas encore de valeur, alors on l'initialise.
            if (!asteroids.hasOwnProperty(matches[0])) {
               asteroids[matches[0]] = {}
            }
            // On recupere la position de la lettre.
            asteroids[matches[0]][times[cursor]] = [i,matches.index]
            // Une fois la lettre et positions recupérées, on enleve la lettre de la ligne.
            entry = entry.replaceAt(matches.index, '.')
        }
    }
}

// Pour chaque asteroid, on cherche t3
for (let letter in asteroids) {
    try {
        // On recupere la distance parcourue entre t1 et t2
        let diff = [
            (asteroids[letter][times[1]][0] - asteroids[letter][times[0]][0]),
            (asteroids[letter][times[1]][1] - asteroids[letter][times[0]][1]),
        ]
        // On cherche le ratio en fonction des temps
        let ratioDiffBis = times[1] - times[0]
        let ratioDiff = times[2] - times[1]
        // On calcule t3 en fonction de la distance parcourue et des ratio calculés via les temps. 
        asteroids[letter][times[2]] = [
            asteroids[letter][times[1]][0] + (diff[0] * ratioDiff)/ratioDiffBis,
            asteroids[letter][times[1]][1] + (diff[1] * ratioDiff)/ratioDiffBis
        ]
        // On arrondi la position de chaque asteroid afin d'éviter les nombres flottants.
        for (let time in asteroids[letter]) {
            asteroids[letter][time] = asteroids[letter][time].map(entry => Math.floor(entry))
        }
    }
    catch(e) { continue; }
}

// On affiche le résultat
for (let i = 0; i < H; i++) {
    let row = (new Array(W)).fill('.').join('')
    for (let [letter,positions] of Object.entries(asteroids).sort().reverse()) {
        if (i === positions[times[2]][0] && W > positions[times[2]][1] && 0 <= positions[times[2]][1]) {
            row = row.replaceAt(positions[times[2]][1], letter)
        }
    }
    console.log(row)
}
