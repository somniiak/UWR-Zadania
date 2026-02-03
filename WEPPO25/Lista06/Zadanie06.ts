// Po co typy wyższego rzędu?
// - Tworzenie elastycznego typu który zadziała w różnych kontekstach.
// - Pomagają manipulować prostszymi typami gdy chcemy z niczh
//   zbudować typy bardziej złożone.
// - Pomagają przy pracy ze złożonymi strukturami danych, takimi jak
//   głęboko zagnieżdżone obiekty lub struktury rekurencyjne, gdy
//   potrzeba sposobu na dynamiczną transformację ich typów. 


// Extract<Union, Type> - wybiera z unii tylko te typy, które można przypisać Type
// Exclude<Union, Type> - usuwa z unii typy przypisywalne do Type

type Car = "Car" | "Truck" | "Bus";

type Bike = "Bike" | "Electric Bike";

type Boat = "Yacht" | "Ferry" | "Sailboat";

type Vehicle = Car | Bike | Boat;

type ContainsEngine = Extract<Vehicle, Car | Boat>;
// Car | Boat

type LandOnly = Exclude<Vehicle, Boat>; 
// Car | Bike


// Record<KeyType, ValueType> - tworzy obiekt z określonymi kluczami i typami wartości
// Required<Type> - zmienia wszystkie pola w typie na wymagane
// Readonly<Type> - zamienia wszystkie pola w typie na tylko do odczytu
// Partial<Type> - wszystkie pola stają się opcjonalne

type User = { name: string; age?: number };

const users: Record<'epicgamer420' | 'pompompurin', User> = {
    epicgamer420: { name: 'Steve', age: 22 },
    pompompurin: { name: 'Edvard', age: 42 },
}

type UserRequired = Required<User>;
const user1: UserRequired = {
    name: 'Kasjusz', age: 25
};

type UserReadonly = Readonly<User>;
const user2: UserReadonly = {
    name: 'Brajan'
};
// user2.name = 'Kasjusz';

type UserPartial = Partial<User>;
const user3: UserPartial = { };


// Pick<Type, Keys> - wybiera pola z typu.
// Omit<Type, Keys> - usuwa wybrane pola z typu

type Address = {
    apartment: number,
    street: string,
    city: string,
    country: string,
    postcode: string,
}

type Place = Pick<Address, 'city' | 'country'>;
// {city: string, country: string}
const place: Place = {
    city: 'Wrocław',
    country: 'Poland',
}

type Region = Omit<Address, 'apartment' | 'country'>;
// {street: string, city: string, postcode: string}
const region: Region = {
    street: 'Kolorowa',
    city: 'Wrocław',
    postcode: 'BB-420',
}


type Video = {
    title: string,
    uploader: string,
    info: {
        date: string,
        views: number,
        likes: number,
    }
}

type VideoInfo = Video['info'];
// {date: string, views: number, likes: numer}