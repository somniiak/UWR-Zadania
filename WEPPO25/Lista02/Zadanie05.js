const Punkt = {
    x: 0,
    y: 0,

    // Właściwość (getter)
    get prettyPrint() {
        return `(${this.x}, ${this.y})`
    },

    // Właściwości (settery)
    set incrementXBy(nx) {
        this.x += nx
    },

    set incrementYBy(ny) {
        this.y += ny
    },

    // Metoda
    distanceFromCenter() {
        return Math.sqrt(
            this.x * this.x + this.y * this.y
        )}
    
    
}

Punkt.incrementXBy = 5
Punkt.incrementYBy = -3
console.log(Punkt.prettyPrint)
console.log(Punkt.distanceFromCenter())


// Dodanie nowego pola
Punkt.distance = Punkt.distanceFromCenter()

// Dodanie nowej metody
Punkt.sumPos = function() {
    return this.x + this.y
}

// get i set musi być dodane przez Object.defineProperty
Object.defineProperty(Punkt, 'isInt', {
    get: function() {
        return this.x % 1 == 0 && this.y % 1 == 0
    },
})

Object.defineProperty(Punkt, 'invert', {
    set: function() {
        this.x = -this.x
        this.y = -this.y
    }
})

Punkt.incrementXBy = 0.2
console.log(Punkt.isInt)