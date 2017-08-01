#!/usr/bin/python3

def lca(root, v1, v2):
    if root.data < v1 and root.data < v2:
        return lca(root.right, v1, v2)
    elif rooot.data > v1 and root.data > v2:
        return lca(root.left, v1, v2)
    return root
