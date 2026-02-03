function fibIt() {
    let a = 0, b = 1;
    return {
        next: function() {
            let res = a;
            [a, b] = [b, a + b];
            return { value: res, done: false };
        }
    };
}

function *fibGen() {
    let a = 0, b = 1;
  
    while (true) {
        yield a;
        [a, b] = [b, a + b]
    }
}

var _it = fibIt();
for (let _result; _result = _it.next(), !_result.done;) {
    if (_result.value >= 100) break;
    console.log(_result.value);
}

for (let i of fibGen()) {
    if (i >= 100) break
    console.log(i)
}