// Sparametryzować generator jako funkcja zwracająca funkcję

function createGenerator(max) {
    return function() {
        var _state = 0;
        return {
            next : function() {
                return {
                    value : _state,
                    done : _state++ >= max
                }
            }
        }
    }
}

var foo1 = {
    [Symbol.iterator] : createGenerator(5)
};

for (var f of foo1)
    console.log(f);

var foo2 = {
    [Symbol.iterator] : createGenerator(10)
};

for (var f of foo2)
    console.log(f);