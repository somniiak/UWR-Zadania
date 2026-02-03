var Person = function(name, surname) {
    if (!name || !surname) {
        throw new Error("Podaj imię i nazwisko!");
    }
    this.name = name;
    this.surname = surname;
}

var Worker = function(name, surname, age) {
    Person.call(this, name, surname);
    this.age = age;
}


// Object.create(Person.prototype) tworzy nową instancję obiektu i ustawia jej wskazany obiekt jako prototyp.
// Nie zmieniamy przy tym oryginalnego Person.prototype
// Zachowuje łańcuch prototypów
// Izoluje prototypy (zmiany w Worker nie wpływają na Person)
// Nie wywołuje konstruktora rodzica
Worker.prototype = Object.create(Person.prototype)
var w = new Worker("Jan", "Kowalski", 30)
console.log(w instanceof Worker) // true
console.log(w instanceof Person) // true

// Worker.prototype i Person.prototype stają się tym samym obiektem.
// Każda zmiana w prototypie Worker (np. dodanie nowych metod) wpłynie również na prototyp Person.
Worker.prototype = Person.prototype
// Teraz Worker.prototype i Person.prototype to ten sam obiekt
console.log(Worker.prototype === Person.prototype)
Worker.prototype.getAge = function() { console.log(this.age); }
var p = new Person("Anna", "Nowak")
p.getAge()

// Wywołuje konstruktor rodzica, co może powodować niepożądane efekty uboczne
Worker.prototype = new Person();
var w = new Worker("Jan", "Kowalski", 30);
console.log(w.name)
console.log(w.surname)
console.log(w.age)