var pipe = (xs, ...fns) => fns.reduce((x, fn) => fn(x), xs)

var map = fn => xs => xs.map(fn)

var take = n => xs => xs.slice(0, n) 

function groupBy(keySelect) {
    return function(xs) {
        var grouped = Object.groupBy(xs, keySelect);
        return Object.keys(grouped).map(
            function(key) {
                var group = grouped[key]
                group.key = key
                return group
            }
        );
    };
}

function sort(keySelect) {
    return function(xs) {
        return xs.sort(
            function(a, b) {
                let keyA = keySelect(a)
                let keyB = keySelect(b)

                if (typeof keyA === 'string' && typeof keyB === 'string')
                    return keyA.localeCompare(keyB)
                if (typeof keyA === 'number' && typeof keyB === 'number')
                    return keyA - keyB
                if (keyA > keyB)
                    return 1
                if (keyA < keyB)
                    return -1
                return 0
            }
        )
    }
} 

var res = pipe(
    [
        {ip: `192.168.0.1`},
        {ip: `192.168.0.1`},
        {ip: `192.168.0.2`},
        {ip: `192.168.0.2`},
        {ip: `192.168.0.3`},
        {ip: `192.168.0.17`},
        {ip: `192.168.0.1`},
    ],
    groupBy(e => e.ip),
    sort(g => -g.length),
    take(3),
    map(a => ({ip: a.key, count: a.length }))
);
console.log(res)