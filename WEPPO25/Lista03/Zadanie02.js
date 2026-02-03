function divisors_imp(n) {
    const res = []
    for (let i = 2; i * i <= n; i++)
        while (n % i == 0) {
            res.push(i);
            n /= i;
        }
    if (n > 1)
        res.push(n);
    return res
}

function divisors_fun(n, i=2, res=[]) {
    if (i * i <= n) {
        if (n % i == 0)
            return divisors_fun(n / i, i, res.concat([i]))
        else
            return divisors_fun(n, i + 1, res)
    }
    if (n > 1)
        return res.concat([n])
    return res
}

console.log(divisors_imp(5))
console.log(divisors_imp(10))
console.log(divisors_fun(5))
console.log(divisors_fun(10))