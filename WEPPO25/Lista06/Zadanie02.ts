function memoize<A, R>(fn: (arg: A) => R): (arg: A) => R {
    const cache = new Map<A, R>();
    
    return (arg: A): R => {
        if (cache.has(arg)) {
            return cache.get(arg)!;
        }
        
        const result = fn(arg);
        cache.set(arg, result);
        return result;
    };
}

const fib = memoize(
    (n: number): number => {
        if (n < 2) return n;
        return fib(n - 1) + fib(n - 2);
    }
);

console.log(fib(40));

// npx tsc Zadanie02.ts > Zadanie02.js
// tsc --watch Zadanie02.ts