class Set:
    def __init__(self, *elems):
        self.tree = []
        pass
            
    def add(self, e):
        add_to_tree(e, self.tree)
        
    def __contains__(self, e):
        return in_tree(self.tree, e)

    def __len__(self):
        return tree_size(self.tree)

    def __and__(self, other):
        return merge(self.tree, other.tree)

    def __sub__(self, other):
        return split(self.tree, other.tree)

def in_tree(tree, e):
    if tree == []:
        return False
    n, left, right = tree
    if n == e:
        return True
    if e < n:
        return in_tree(left, e)
    return in_tree(right, e)

def tree_to_list(tree):
    if tree == []:
        return []
    n, left, right = tree
    return tree_to_list(left) + [n] + tree_to_list(right)

def add_to_tree(e, tree, prev=[]):
    if not tree:
        tree.append(e)
        tree.append([])
        tree.append([])

    else:
        if e == tree[0]:
            return
        add_to_tree(e, tree[2], prev)

def tree_size(tree):
    c = 1
    if tree:
        c += tree_size(tree[2])
    else:
        return 0
    return c

def merge(ltree, rtree):
    ltree = tree_to_list(ltree)
    rtree = tree_to_list(rtree)
    tmptree = ltree + rtree
    res = Set()
    for e in tmptree:
        res.add(e)
    return res

def split(ltree, rtree):
    res = Set()
    for e in tree_to_list(ltree):
        if not in_tree(rtree, e):
            res.add(e)
    return res

x = Set()
x.add(4); x.add(5); x.add(1)
x.add(9); x.add(4); x.add(8)
print(tree_to_list(x.tree))
print(len(x), '\n')

y = Set()
y.add(1); y.add(4); y.add(5)
y.add(7); y.add(3); y.add(2)
print(tree_to_list(y.tree))
print(len(y), '\n')

a = x & y
print(tree_to_list(a.tree), len(a))
b = x - y
print(tree_to_list(b.tree), len(b))