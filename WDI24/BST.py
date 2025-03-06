from random import randint

class TreeItem:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def printTree(root, indent="", position="Root"):
    if root:
        print(f"{indent}[{position}] - {root.val}")
        indent += "   "
        printTree(root.left, indent, "L")
        printTree(root.right, indent, "R")

def write(root):
    if root:
        write(root.left)
        print(root.val, end=' ')
        write(root.right)

def sizeof(root, skey):
    if not root:
        return 0
    
    elif skey < root.val:
        return sizeof(root.left, skey)
    
    elif skey > root.val:
        return sizeof(root.right, skey)
    
    elif skey == root.val:
        count = 1

        if root.left:
            count += sizeof(root.left, root.left.val)

        if root.right:
            count += sizeof(root.right, root.right.val)

        return count

def height(root, skey, depth=1):
    if not root:
        return 0
    
    elif skey < root.val:
        return height(root.left, skey, depth)
    
    elif skey > root.val:
        return height(root.right, skey, depth)
    
    elif skey == root.val:
        if root.left:
            ldepth = height(root.left, root.left.val, depth + 1)
        else:
            ldepth = depth
        
        if root.right:
            rdepth = height(root.right, root.right.val, depth + 1)
        else:
            rdepth = depth

        if ldepth < rdepth:
            return rdepth
        else:
            return ldepth


def insert(root, nkey):
    if not root:
        return TreeItem(nkey)
    
    elif nkey < root.val:
        root.left = insert(root.left, nkey)
    
    elif nkey > root.val:
        root.right = insert(root.right, nkey)
    
    return root

def append(root, nkey):
    if not root:
        root = TreeItem(nkey)

    child = root
    parent = child

    while child:
        parent = child

        if nkey < child.val:
            child = child.left

        elif nkey > child.val:
            child = child.right
        
        elif nkey == child.val:
            return

    if nkey < parent.val:
        parent.left = TreeItem(nkey)
    else:
        parent.right = TreeItem(nkey)

def pop(root, dkey):
    child = root
    parent = None

    while child:
        if dkey < child.val:
            parent = child
            child = child.left

        elif dkey > child.val:
            parent = child
            child = child.right
        
        elif dkey == child.val:
            break
    
    if not child:
        return
    
    if child.val < parent.val:
        rest = child.right
        parent.left = child.left

    elif child.val > parent.val:
        rest = child.left
        parent.right = child.right

    if rest:
        current = parent
        while current:
            parent = current

            if rest.val < current.val:
                current = current.left

            elif rest.val > current.val:
                current = current.right

        if rest.val < parent.val:
            parent.left = rest

        elif rest.val > parent.val:
            parent.right = rest

def is_valid(root):

    if not root.left and not root.right:
        return True
    
    elif not root.left:
        if root.val < root.right.val:
            return True
    
    elif not root.right:
        if root.val > root.left.val:
            return True

    elif is_valid(root.left) and is_valid(root.right):
        if root.left.val < root.val < root.right.val:
            return True

    return False

def list_items(root, skey):
    if not root:
        return

    elif skey < root.val:
        return list_items(root.left, skey)

    elif skey > root.val:
        return list_items(root.right, skey)

    elif skey == root.val:
        if root.left:
            list_items(root.left, root.left.val)
        print(root.val, end=' ')
        if root.right:
            list_items(root.right, root.right.val)

def swap(root, skey, parent=None):
    if skey < root.val:
        return swap(root.left, skey, parent=root)

    elif skey > root.val:
        return swap(root.right, skey, parent=root)

    elif skey == root.val:
        u = root
        v = u.left

        if not v:
            return

        u.left = v.right
        v.right = u

        if not parent:
            root.val = v.val
            root.left = v.left
            root.right = u.right

        elif v.val < parent.val:
            parent.left = v

        elif v.val > parent.val:
            parent.right = v


drzewo = TreeItem(5)
insert(drzewo, 4)
insert(drzewo, 10)
insert(drzewo, 3)
insert(drzewo, 7)
insert(drzewo, 11)
insert(drzewo, 6)
insert(drzewo, 9)
append(drzewo, 1)
append(drzewo, 15)
append(drzewo, 16)
pop(drzewo, 10)
printTree(drzewo)
swap(drzewo, 3)
swap(drzewo, 5)
swap(drzewo, 11)
printTree(drzewo)