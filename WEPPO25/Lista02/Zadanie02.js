// Użycie operatorów . oraz [] do odwoływania się do składowych obiektu
// https://stackoverflow.com/questions/4968406/javascript-property-access-dot-notation-vs-brackets

const pizza = {
    toppings: ['cheese', 'sauce', 'pepperoni'],
    crust: 'deep dish',
    serves: 2,
}

console.log(pizza.toppings)
console.log(pizza['toppings'])

// Użycie argumentów innego typu niż string dla operatora [] dostępu do składowej obiektu
pizza[5] = 'pięć' // Klucz w obiekcie jest więc zawsze typu string. Liczba w argumencie jest też zamieniana na string
pizza[{}] = 'obiekt' // Obiekt zamianiany na string w postaci [object Object]
console.log(pizza)


// Użycie argumentów innego typu niż number dla operatora [] dostępu do tablicy
let pizzaToppings = ['tomato sauce', 'cheese', 'pepperoni']
console.log(pizzaToppings[0])
console.log(pizzaToppings['0'])
pizzaToppings['idx'] = 99 // Tablica w JavaScript jest obiektem i stringiem dodajemy do niej nową właściwość
pizzaToppings[{}] = 19 // Obiekty jest rzutowany na string i powstaje zwykła właściwość o nazwie [object Object], nie element tablicy
console.log(pizzaToppings.length) // Dodanie kluczy nieliczbowych nie zmienia length (bo so dodawane własności, nie elementy tablicy)
pizzaToppings.length = 5 // Rozszerzamy pustymi wartościami
console.log(pizzaToppings)
pizzaToppings.length = 3 // Skracamy do n pierwszych elementów
console.log(pizzaToppings)