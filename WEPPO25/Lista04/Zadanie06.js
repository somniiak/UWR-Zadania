function Tree(val, left, right) {
    this.val = val
    this.left = left
    this.right = right
}

Tree.prototype[Symbol.iterator] = function*() {
    yield this.val

    if (this.left)
        yield* this.left

    if (this.right)
        yield* this.right
}

var root = new Tree(
    1,
    new Tree(
        2,
        new Tree(3),
        new Tree(5),
    ),
    new Tree(
        7,
        new Tree(9),
        new Tree(8),
    )
);

// var stack = []
// stack.push(1)
// var value = stack.pop()

// var queue = [];
// queue.push(1);
// var value = queue.shift()

Tree.prototype[Symbol.iterator] = function* () {
    const queue = [this];
    while (queue.length > 0) {
        const node = queue.shift();

        if (node.left)
            queue.push(node.left)
        if (node.right)
            queue.push(node.right)

        yield node.val
    }
}

for (let e of root) {
    console.log(e)
}