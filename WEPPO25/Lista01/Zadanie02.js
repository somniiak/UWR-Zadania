function sumDigits(n) {
    if (n < 0)
        return sumDigits(-n);
    else if (n == 0)
        return 0;
    else {
        return n % 10 + sumDigits((n - n % 10) / 10);
    }
}

function listDigits(n) {
    if (n < 0)
        return listDigits(-n);
    else {
        let res = [];

        do {
            res.push(n % 10);
            n = (n - n % 10) / 10;
        } while (n > 0)

        return res;
    }
}

function isDivisibleDigits(n) {
    for (let digit of listDigits(n)) {
        if (digit == 0)
            return false;
        if (n % digit != 0)
            return false;
        n /= digit;
    }

    return true;
}

let res = []
for (let i = 1; i <= 100000; i++) {
    if (i % sumDigits(i) == 0)
        if (isDivisibleDigits(i))
            res.push(i);
}
console.log(res);