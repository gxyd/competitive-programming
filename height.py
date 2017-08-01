#!/usr/bin/python3

def height(root):
    if root.left is None and root.right is None:
        return 0
    elif root.left is None and root.right is not None:
        return 1 + height(root.right)
    elif root.right is None and root.left is not None:
        return 1 + height(root.left)
    else:
        return 1 + max(height(root.left), height(root.right))
