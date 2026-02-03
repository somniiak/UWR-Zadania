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

function *take(f, n) {
    for (let i = 0; i < n; i++) {
        const {value, done} = f.next();
        if (done) return
        else yield value
    }
}

for (let num of take(fibIt(), 5)) {
    console.log(num);
}

for (let num of take(fibGen(), 5)) {
    console.log(num);
}