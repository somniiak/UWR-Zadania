function getLastProto(o) {
    var p = o;
    do {
        o = p;
        p = Object.getPrototypeOf(o);
    } while (p);

    return o;
}

const myStr = "hello";
const myNum = 42;
const myBool = true;
const myObj = {};

for (var i of [myStr, myNum, myBool, myObj]) {
    for (var j of [myStr, myNum, myBool, myObj]) {
        console.log(i + " oraz " + j + " = ", getLastProto(i) == getLastProto(j))
    }
}