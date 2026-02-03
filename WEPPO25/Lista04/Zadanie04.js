// Wartości typów prostych nie są obiektami. Są niemutowalne i nie mają własnych
// właściwości ani metod. Gdy wywołuje się na nich metodę lub próbuje się
// uzyskać wartość silnik tymczasowo opakowuje je w odpowieni obiekt (Number, String,
// Boolean, ...) po czym ten obiekt jest natychmiast niszczony. 

var n = 1

// liczba ma prototyp?
console.log(typeof Object.getPrototypeOf(n));

// można jej dopisać pole/funkcję?
// n.foo = 'foo'

Object.defineProperty(Object.prototype, 'sayHello', {
    get: _ => "Hello world!"
})

var p = 2
console.log(p.sayHello)