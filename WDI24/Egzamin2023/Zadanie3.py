class TreeItem:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

r = TreeItem(1)
r.right = TreeItem(7)
r.right.right = TreeItem(19)
r.left = TreeItem(9)
r.left.left = TreeItem(11)
r.left.left.left = TreeItem(4)
r.left.right = TreeItem(3)
r.left.right.left = TreeItem(2)
r.left.right.left.right = TreeItem(5)

def sumaPN(r, level=0):
    if not r:
        return 0

    if level % 2:
        return -r.val + sumaPN(r.left, level + 1) + sumaPN(r.right, level + 1)
    else:
        return r.val + sumaPN(r.left, level + 1) + sumaPN(r.right, level + 1)

print(sumaPN(r))