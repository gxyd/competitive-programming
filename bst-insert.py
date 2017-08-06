#!/usr/bin/python3

def insert(root, val):
    if root:
        _insert(root, val)
    else:
        root = Node(val)
    return root


def _insert(root, val):
    if root.data > val:
        if root.left:
            _insert(root.left, val)
        else:
            r = Node(val)
            root.left = r
    else:
        if root.right:
            _insert(root.right, val)
        else:
            r = Node(val)
            root.right = r
