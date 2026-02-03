type Person = {
    name: string,
    surname: string,
}

type Animal = {
    name: string,
    species: string,
}

// Obiekt musi mieć wszystkie pola z `Person` i `Animal`
type PersonAndAnimal = Person & Animal;

((obj: PersonAndAnimal): void =>
    console.log(`${obj.name} ${obj.surname} to ${obj.species}.`)
)({
    name: "Nick",
    surname: "Wilde",
    species: "lis"
});

// Bezsens - `never`
type PersonAndString = Person & string;

// Obiekt może być `Person` lub `Animal`
type PersonOrAnimal = Person | Animal;

((obj: PersonOrAnimal): void => {
    if ('surname' in obj)
        console.log(`Człowiek ${obj.name} ${obj.surname}`);
    else
        console.log(`Zwierzę gatunku ${obj.species}.`);
})({
    name: "Laura",
    surname: "Palmer",
});

// Obiekt może być `Person` lub stringiem
type PersonOrString = Person | string;

((obj: PersonOrString): void => {
    if (typeof obj === 'string')
        console.log(`string ${obj}`);
    else
        console.log(`Osoba ${obj.name} ${obj.surname}.`);
})("Onomatopeja");

// Bezsens - `never`
type StringAndNumber = string & number;

// Obiekt może być stringiem lub liczbą
type StringOrNumber = string | number;

((obj: StringOrNumber): void => {
    if (typeof obj === 'string')
        console.log(`string ${obj}`)
    else
        console.log(`liczba ${obj}`)
})(4);


