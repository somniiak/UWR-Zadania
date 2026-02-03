// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty
// The `hasOwnProperty()` method of Object instances returns a boolean
// indicating whether this object has the specified property as its own
// property (as opposed to inheriting it).

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn
// The Object.hasOwn() static method returns true if the specified object
// has the indicated property as its own property. If the property is inherited,
// or does not exist, the method returns false.

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys
// The Object.keys() static method returns an array of a given object's own
// enumerable string-keyed property names.

function getLastProto(o) {
    var p = o;
    do {
        o = p;
        p = Object.getPrototypeOf(o);
    } while (p);

    return o;
}

var isInherited = (obj, field) => !obj.hasOwnProperty(field)

// Zwraca pola/funkcje występujące w obiekcie
var getOwnProperties = obj => Object.keys(obj)

// Zwraca pola/funkcje występujące w obiekcie oraz jego łańcuchu prototypów
function getPropProperties(obj) {
    let res = [];

    while (obj) {
        res.push(...getOwnProperties(obj));
        obj = Object.getPrototypeOf(obj);
    }

    return res;
}

var p = { name: 'jan' }
var q = { surname: 'kowalski' }
Object.setPrototypeOf(p, q);

console.log('własne:', getOwnProperties(p));
console.log('z prototypami:', getPropProperties(p));
console.log('czy name odziedziczone dla p?', isInherited(p, 'name'));
console.log('czy surname odziedziczone dla p?', isInherited(p, 'surname'));