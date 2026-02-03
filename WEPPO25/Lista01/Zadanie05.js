function fibRec(n) {
    if (n < 1)
        return 0;
    else if (n == 1)
        return 1;
    else
        return fibRec(n - 1) + fibRec(n - 2);
}

function fibIter(n) {
    let prev1 = 0;
    let prev2 = 1;
    let curr = 0;

    for (let i = 0; i < n; i++) {
        prev1 = prev2;
        prev2 = curr;
        curr = prev1 + prev2;
    }

    return curr;
}

// https://stackoverflow.com/questions/12492979/how-to-get-the-output-from-console-timeend-in-js-console
res = []
for (let n = 10; n <= 40; n += 5) {
  const startRec = performance.now();
  fibRec(n);
  const endRec = performance.now();

  const startIter = performance.now();
  fibIter(n);
  const endIter = performance.now();

  res.push({
        n,
        fibRec: (endRec - startRec).toFixed(4) + " ms",
        fibIter: (endIter - startIter).toFixed(4) + " ms",
    });
}

console.table(res);