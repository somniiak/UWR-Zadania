function fibRecMemo(n, cache={}) {
    if (n in cache)
        return cache[n]
    else if (n <= 1)
        return n;
    cache[n] = (
        fibRecMemo(n - 1, cache) +
        fibRecMemo(n - 2, cache)
    )
    return cache[n]
}

function fibRec(n) {
  if (n <= 1) return n;
  return fibRec(n - 1) + fibRec(n - 2);
}

console.log(fibRecMemo(40))